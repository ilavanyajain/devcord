from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    password = models.CharField(max_length=128, blank=True, null=True)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)