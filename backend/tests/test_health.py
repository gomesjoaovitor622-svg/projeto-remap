from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_liveness_returns_alive() -> None:
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_returns_ready_when_database_connects() -> None:
    connection = MagicMock()
    connection.__enter__.return_value = connection

    with patch("app.main.engine.connect", return_value=connection):
        response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "database": "connected"}


def test_readiness_returns_503_when_database_is_unavailable() -> None:
    from sqlalchemy.exc import OperationalError

    with patch(
        "app.main.engine.connect",
        side_effect=OperationalError("SELECT 1", {}, Exception("database unavailable")),
    ):
        response = client.get("/health/ready")

    assert response.status_code == 503
    assert response.json()["detail"] == "Banco de dados indisponível."
