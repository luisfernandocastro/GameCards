from django.contrib.auth.models import AbstractUser
from django.db import models

#modelo usuarios 

class User(AbstractUser):
    email = models.EmailField('correo Electronico',unique=True)

    USERNAME_FIELD = 'email' #email 
    REQUIRED_FIELDS = ['username'] #nombre de usuarios