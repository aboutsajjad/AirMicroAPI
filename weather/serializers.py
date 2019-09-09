from rest_framework.serializers import ModelSerializer
from weather.models import Weather


class WeatherSerializer(ModelSerializer):
    class Meta:
        model = Weather
        exclude = ()
