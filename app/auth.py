import os
import jwt

from fastapi import security
from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from dotenv import load_dotenv
from datetime import datetime, timedelta
from passlib.context import CryptContext

load_dotenv()


class Auth_handler():
    security = HTTPBearer()
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    refresh_token_secret = os.environ["REFRESH_TOKEN_SECRET"]
    pwdContext = CryptContext(schemes=["bcrypt"])

    # hash password func
    def get_hashed_password(self, password):
        return self.pwdContext.hash(password)

    # verify user password match hashed password
    def verify_password(self, user_password, hashed_password):
        return self.pwdContext.verify(hashed_password, user_password)

    # create access_token
    def create_access_token(self, user_id):
        payload = {
            "ext": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, self.access_token_secret, algorithm="HS256")

    # create refresh_token
    def create_refresh_token(self, user_id):
        payload = {
            "ext": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, self.refresh_token_secret, algorithm="HS256")

    # verify access_token
    def decode_access_token(self, token):
        try:
            payload = jwt.decode(token, self.access_token_secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=402, detail="Invalid token")

    # verify refresh_token
    def decode_refresh_token(self, token):
        try:
            payload = jwt.decode(token, self.refresh_token_secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=402, detail="Invalid token")

    # wrapper
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_access_token(auth.credentials)
