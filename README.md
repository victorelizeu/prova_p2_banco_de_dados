# 🚀 API de Gerenciamento de Pedidos

API desenvolvida com **FastAPI** para gerenciamento assíncrono de pedidos.

### Tecnologias Utilizadas

- ⚡ FastAPI
- 🍃 MongoDB (persistência/banco de dados)
- 🐇 RabbitMQ / Kafka (mensageria)
- 🐳 Docker (containerização)

---

## 🔗 Links de Acesso

### API (Swagger UI)

http://localhost:8000/docs

### RabbitMQ (Painel Administrativo)

http://localhost:15672

**Credenciais padrão:**

- Usuário: `guest`
- Senha: `guest`

---

## 🧪 Como Testar

Para garantir a conexão correta com o banco de dados e os serviços de mensageria dentro do ambiente Docker, execute:

```bash
docker compose exec api pytest
```

---

## 🛑 Como Encerrar

Para derrubar os contêineres e liberar as portas utilizadas:

```bash
docker compose down
```

---

## 👨‍💻 Autor

**João Victor Elizeu Silva**

Graduando em **Engenharia de Software (5º período)** pela **Universidade de Vassouras**, campus Maricá.
