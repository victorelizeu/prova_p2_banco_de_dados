from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_post(client):
    response = client.post(
        "/pedidos",
        json={
            "nome_cliente": "Jones",
            "nome_produto": "iPhone 14",
            "quantidade": 1,
        },
    )
    assert response.status_code == 200
    assert "ID" in response.json()


def test_get(client):
    response = client.get("/pedidos")
    assert response.status_code == 200
    assert "Pedidos" in response.json()
