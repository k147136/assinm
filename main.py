import uricorn
from fastapi import FastAPI
app = FastAPI()
database = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def read_items():
        return database