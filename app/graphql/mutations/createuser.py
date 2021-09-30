import graphene

from app.models import User
from app.schemas import Create_user_schema
from app.graphql.gqlmodel.user_model import UserModel
from app.auth import Auth_handler
from app.config.db import db_session

db = db_session.session_factory()

authHandler = Auth_handler()

class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    newUser = graphene.List(UserModel)

    @staticmethod
    def mutate(root, info, email, username, password):
        # hash pwd
        hashed_password = authHandler.get_hashed_password(password)

        # collect args
        user = Create_user_schema(email=email, username=username, password=hashed_password)
        newUser = User(email=user.email, username=user.username, password=user.password)

        # add to db
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        ok = True

        return CreateUser(ok=ok)