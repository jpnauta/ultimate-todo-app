from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from modules.users.models import User


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
