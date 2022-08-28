from operator import truediv
from unicodedata import name
from django.db import models

class Musician(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Album (models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    release_date = models.DateField()
    num_stars = models.IntegerField()


