import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

SECRETS_ROUTE = "/run/secrets/"

@app.get("/")
async def root():
    return {"Response": "App works"}

@app.get("/envtest")
def envtest():
    return {"Environmental variables": os.environ["envFoo"]}

@app.get("/secrettest")
def secrettest():
    with open(SECRETS_ROUTE + "some_key") as f:
        line = f.readline()
        return {"Secrets": line}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
    #Secretos en /run/secrets/