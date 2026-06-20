# 🏪 API de Gerenciamento de Pedidos para a empresa Eletronic Models, Inc

API desenvolvida com **FastAPI** para gerenciamento assíncrono de pedidos. Eu coloquei um nome fictício de Eletronic Models, Inc para a empresa, mas é editável.

### Tecnologias

- FastAPI
- MongoDB (persistência/banco de dados)
- RabbitMQ / Kafka (mensageria)
- Docker (containerização)

---

## Links de Acesso

### API (Swagger UI)

http://localhost:8000/docs

### RabbitMQ (Painel Administrativo)

http://localhost:15672

**Credenciais:**

- Usuário: `guest`
- Senha: `guest`

---

## Como Testar

Para garantir a conexão correta com o banco de dados e os serviços de mensagem dentro do ambiente Docker, execute:

```bash
docker compose exec api pytest
```

---

## Como Encerrar

Para derrubar os contêineres e liberar as portas utilizadas:

```bash
docker compose down
```

---

## 👨‍💻 Autor

**João Victor Elizeu Silva**

Graduando em **Engenharia de Software (5º período)** pela **Universidade de Vassouras**, campus Maricá.
