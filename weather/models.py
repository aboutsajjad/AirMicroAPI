from django.db import models


class Weather(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    altitude = models.FloatField()
    mics5524 = models.FloatField()
