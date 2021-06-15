from fastapi import FastAPI
from typing import Optional

# Create the core of the API
app = FastAPI()

# Add different endpoints together with the http verb/request declaring what we want from the server
# Here we only have GET requests, so we only want the server to send us back data


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def root():
    return {"message": "It really works!!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
