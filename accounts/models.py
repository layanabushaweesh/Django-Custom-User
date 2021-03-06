from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    email = models.EmailField(('email address'), unique=True) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    

    def __str__(self):
        return self.username