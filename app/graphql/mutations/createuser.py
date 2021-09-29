import graphene

from app.models import User
from app.schemas import Create_user_schema
from app.graphql.gqlmodel.create_user_model import CreateUserModel
from app.auth import Auth_handler

authHandler = Auth_handler()

class CreateNewUser(graphene.Mutation):
    class Argument:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    new_user = graphene.List(CreateUserModel)

    @staticmethod
    def mutate(root, info, email, username, password):
        # hash pwd
        hashed_password = Auth_handler.get_hashed_password(password)

        # collect args
        user = Create_user_schema(email=email, username=username, password=hashed_password)
        new_user = User(email=user.email, username=user.username, password=user.password)

        # add to db
        # db.add(new_user)
        # db.commit()
        # db.refresh(new_user)

        print(new_user.password)

        return ok
        pass