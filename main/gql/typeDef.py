from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
from main.models import  Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id','user','title','description','status','created_on',)


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('id','username','tasks') #if it fails change it to tasks