import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from modules.users.schemas import UserType


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserType)
    user = graphene.Field(UserType)


schema = graphene.Schema(query=Query, types=[UserType])
