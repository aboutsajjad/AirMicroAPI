from django.db import models
from utils.base_model import BaseModel
from meteocalc import Temp, dew_point, heat_index


class Weather(BaseModel):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    mics5524 = models.FloatField()

    @property
    def temp(self):
        return Temp(self.temperature, 'C')

    @property
    def dew_point(self):
        return dew_point(temperature=self.temp, humidity=self.humidity).c

    @property
    def heat_index(self):
        return heat_index(temperature=self.temp, humidity=self.humidity).c

    @property
    def altitude(self):
        return 1000
