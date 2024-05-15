from django import forms
from django.contrib.auth.forms import UserCreationForm     
from .models import user

class UserForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']
 