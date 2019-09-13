from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from weather.models import Weather
from weather.serializers import WeatherSerializer


class WeatherListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WeatherSerializer
    queryset = Weather.objects.order_by('-id').all()
