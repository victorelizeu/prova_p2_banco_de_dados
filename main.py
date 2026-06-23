from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import motor.motor_asyncio
import pika
import json
from confluent_kafka import Producer

app = FastAPI(title="API da Eletronic Models, Inc. by: Jones")

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongodb:27017")

db = client.mongodb

kafka_config = {"bootstrap.servers": "kafka:9092"}
kafka_producer = Producer(kafka_config)


@app.get("/")
def Home():
    return {"msg": "Seja Bem-Vindo!"}


class Pedido(BaseModel):
    nome_cliente: str
    nome_produto: str
    quantidade: int
    status: str = "PENDENTE"


@app.post("/pedidos", status_code=status.HTTP_201_CREATED)
async def post_pedido(novo_pedido: Pedido):
    pedido = novo_pedido.model_dump()

    res = await db.pedidos.insert_one(pedido)

    id_gerado = str(res.inserted_id)

    conexao = pika.BlockingConnection(pika.ConnectionParameters(host="rabbit"))
    canalizacao = conexao.channel()

    fila = canalizacao.queue_declare(queue="pedidos_postados")

    mensagem = {"id": id_gerado, "status": "Está_Pendente"}

    msgjson = json.dumps(mensagem)

    canalizacao.basic_publish(exchange="", routing_key="pedidos_postados", body=msgjson)

    conexao.close()

    def delivery_report(err, msg):
        if err is not None:
            print(f"Erro! {err}")

    kafka_producer.produce("produtos", msgjson, callback=delivery_report)

    kafka_producer.flush()

    return {"msg": "Pedido postado e ID gerado!", "ID": id_gerado}


@app.get("/pedidos", status_code=status.HTTP_200_OK)
async def visualizar_pedidos():
    pedidos = await db.pedidos.find().to_list(length=100)

    pedidos_formatados = []

    for p in pedidos:
        p["_id"] = str(p["_id"])

        pedidos_formatados.append(p)

    return {"msg": "Visualização de Pedidos!", "Pedidos": pedidos_formatados}
