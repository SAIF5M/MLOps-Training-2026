from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_model_info():
    response = client.get("/model/info")
    assert response.status_code == 200
    assert "version" in response.json()