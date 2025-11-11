from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    payload = {"X": [[5.1, 3.5, 1.4, 0.2]]}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "y" in body and isinstance(body["y"], list)
