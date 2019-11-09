from django.db import models
from main.models import Washer,Dryer
from account.models import User

class W_Book(models.Model):
    MachineId = models.ForeignKey(Washer, on_delete=models.CASCADE)
    #UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    UserId = models.IntegerField()
    ValidTime = models.DateTimeField()
    EndTime = models.DateTimeField(null=True,blank=True)

class D_Book(models.Model):
    MachineId = models.ForeignKey(Dryer, on_delete=models.CASCADE)
    #UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    UserId = models.IntegerField()
    ValidTime = models.DateTimeField()
    EndTime = models.DateTimeField(null=True,blank=True)