from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def accueil():
    return {"message": "Bonjour depuis ci-demo"}

@app.get("/addition")
def addition(a: int, b: int):
    return {"resultat": a + b}