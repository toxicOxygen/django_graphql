import graphene
from main.gql.query import Query as MainQuery


class Query(MainQuery,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)