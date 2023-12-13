from django.db import models
from django.contrib.auth.models import AbstractUser

from main.managers import TakugoUserManager

# Create your models here.
class TakugoUser(AbstractUser):
    user_type = models.CharField(max_length=1)
    
    objects = TakugoUserManager()

    def is_regular(self):
        return self.user_type == "U"

    def is_institution(self):
        return self.user_type == "I"

    def __str__(self):
        return self.username
