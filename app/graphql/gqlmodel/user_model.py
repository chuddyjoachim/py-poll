from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User

class UserModel(SQLAlchemyObjectType):
    class Meta:
        model = User
        exclude_fields = [
            'created_at',
            'password',
        ]
