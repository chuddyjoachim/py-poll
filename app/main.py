import uvicorn

from fastapi import FastAPI
from app.graphql import schema
from app.config.db import db_session
from app.auth import Auth_handler

from starlette.graphql import GraphQLApp

db = db_session.session_factory()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.add_route("/graphql", GraphQLApp(schema=schema))

if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
