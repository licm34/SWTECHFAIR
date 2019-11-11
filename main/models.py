from django.db import models

class Washer(models.Model):
    PLACE_CHOICES = (
        ('1','308관 남자'),
        ('2','309관 남자'),
        ('3','308관 여자'),
        ('4','309관 여자'),
    )

    Place = models.CharField(max_length=10,choices=PLACE_CHOICES) 
    Number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Number)+'번 세탁기'

class Dryer(models.Model):
    PLACE_CHOICES = (
        ('1','308관 남자'),
        ('2','309관 남자'),
        ('3','308관 여자'),
        ('4','309관 여자'),
    )
    Place = models.CharField(max_length=10,choices=PLACE_CHOICES) #308M,308F,309M,309F
    Number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Number)+'번 건조기'