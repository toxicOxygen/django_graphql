import graphene
from .typeDef import TaskType,UserType
from main.models import Task
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

class Query:
    all_tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType,id=graphene.ID())

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType,id=graphene.Int())

    def resolve_all_tasks(self,info,**kwargs):
        return Task.objects.all()
    
    def resolve_task(self,info,**kwargs):
        try:
            return Task.objects.get(id=kwargs.get('id'))
        except ObjectDoesNotExist:
            return None
    
    def resolve_all_users(self,info,**kwargs):
        return get_user_model().objects.all()
    
    def resolve_user(self,info,**kwargs):
        try:
            return get_user_model().objects.get(id=kwargs.get('id'))
        except:
            return None
        