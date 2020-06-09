from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='tasks')
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title