from pydantic import BaseModel

class Create_user_schema(BaseModel):
    email: str
    username: str
    password: str

class Login_user_schema(BaseModel):
    email: str
    password: str


