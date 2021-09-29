import graphene
import app.models as models

from graphene import ObjectType, String, Field, List
from graphene_federation import build_schema

from app.config.db import db_session

from app.graphql.mutations.createuser import CreateNewUser
from app.graphql.gqlmodel.user_model import UserModel

db = db_session.session_factory()

class Query(ObjectType):

    all_user = List(UserModel)
    user_by_email = Field(UserModel, email=String(required=True))

    def resolve_all_user(self, info):
        query = UserModel.get_query(info)
        print(query)
        return query.all()

    def resolve_user_by_email(self, info, email):
        return db.query(models.User).filter(models.User.email == email).first()


class Mutation(graphene.ObjectType):
    create_new_user = CreateNewUser.Field()


schema = build_schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)