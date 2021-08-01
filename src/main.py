from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome": "FastAPI"}


@app.get("/items/{id}")
def read_item(id: int, query: Optional[str] = None):
    return {"id": id, "query": query}