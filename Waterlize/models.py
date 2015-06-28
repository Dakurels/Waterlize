from django.db import models

class Doors(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    color = models.CharField(max_length=30)

class Temperature(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    temp = models.IntegerField()
