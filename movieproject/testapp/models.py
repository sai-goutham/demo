from django.db import models

# Create your models here.
class movie(models.Model):
    rdate=models.DateField()
    name=models.CharField(max_length=40)
    hero=models.CharField(max_length=40)
    herione=models.CharField(max_length=40)
    rating=models.IntegerField()
