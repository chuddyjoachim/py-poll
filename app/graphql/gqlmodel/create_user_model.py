from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User

class CreateUserModel(SQLAlchemyObjectType):
    class Meta:
        model = User
        exclude_fields = [
            'id',
            'created_at', 
            'updated_at'
        ]