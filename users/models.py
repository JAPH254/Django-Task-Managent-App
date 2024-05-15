from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):  
    last_login = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default.jpg')
    phone_number = models.CharField(max_length=15, null=True)
    bio = models.TextField(null=True)
    nickname = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.username
    
