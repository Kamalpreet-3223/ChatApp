from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Messages(models.Model):
    message = models.CharField(max_length=1000)
