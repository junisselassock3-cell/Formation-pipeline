from fastapi.testclient import Testclient
from main import app

client = Testclient(app)

def test_accueil():
    r = client.get("/")
    assert r.status_code == 200
def test_addition():
    r = client.get("/addition?a=2&b=3")
    assert r.json() == {"resultat": 5}    
