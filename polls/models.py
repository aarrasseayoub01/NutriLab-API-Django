from django.db import models

# Create your models here.


class Food(models.Model):

    name = models.CharField(max_length=200)
    Protein = models.FloatField()
    Calories = models.FloatField()
    Sugar = models.FloatField()
    Salt = models.FloatField()
    Carbs = models.FloatField()
    Fat = models.FloatField()
    Fiber = models.FloatField()
