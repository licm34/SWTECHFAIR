from django.db import models

class Washer(models.Model):
    Place = models.CharField(max_length=4) #308M,308F,309M,309F
    Number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Number)+'번 세탁기'

class Dryer(models.Model):
    Place = models.CharField(max_length=4) #308M,308F,309M,309F
    Number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Number)+'번 건조기'