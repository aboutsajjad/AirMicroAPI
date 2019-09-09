from django.db import models
from utils.base_model import BaseModel


class Weather(BaseModel):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    altitude = models.FloatField()
    mics5524 = models.FloatField()
