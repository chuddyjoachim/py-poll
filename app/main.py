import uvicorn

from typing import Optional
from fastapi import FastAPI

from starlette.graphql import GraphQLApp

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)