from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_returns_welcome_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SchoolHealth API"}


def test_health_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_swagger_docs_are_available() -> None:
    response = client.get("/docs")

    assert response.status_code == 200
