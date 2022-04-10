from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    

    def __str__(self):  
        return self.message
