from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
import random

# Create your models here.
class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    birthday = models.DateField()
    num = models.IntegerField(default=random.randint(1, 100))
    REQUIRED_FIELDS = ['username', 'birthday']


