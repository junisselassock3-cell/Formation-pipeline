from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_accueil():
    r = client.get("/")
    assert r.status_code == 200
def test_addition():
    r = client.get("/addition?a=2&b=3")
    assert r.json() == {"resultat": 5}    
