from django.db import models
from main.models import Washer,Dryer
from account.models import User

class W_Book(models.Model):
    MachineId = models.IntegerField(default=0)
    UserId = models.CharField(max_length=9)
    ValidTime = models.DateTimeField()
    EndTime = models.DateTimeField(null=True,blank=True)

class D_Book(models.Model):
    MachineId = models.IntegerField(default=0)
    UserId = models.CharField(max_length=9)
    ValidTime = models.DateTimeField()
    EndTime = models.DateTimeField(null=True,blank=True)