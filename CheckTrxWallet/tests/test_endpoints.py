import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def client():
    """Создаём тестовый клиент для FastAPI"""
    with TestClient(app) as client:
        yield client


@pytest.mark.asyncio
async def test_get_wallets_endpoint(client):
    """
    Проверяет, что эндпоинт `/wallets-requests`
    корректно отвечает и возвращает данные.
    """
    response = client.get("/wallets-requests?limit=10&offset=0")
    assert response.status_code == 200