from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    message = response.json()["message"]
    # assert message.startswith("Hello from CI/CD Pipeline!")
    assert "PRODUCTION CI/CD PIPELINE" in message
    assert "Hits:" in message

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "hits_total" in response.text