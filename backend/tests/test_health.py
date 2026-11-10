from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert body["service"] == "CCE Backend"
    assert body["version"] == "0.1.0"
    assert "timestamp" in body
