from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, unique=True)
