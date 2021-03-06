from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
  username = forms.CharField(required=True, max_length=30, ) 
  
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2',]

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('message',)

