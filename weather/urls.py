from django.urls import path
from weather.apis import WeatherListCreateAPIView

urlpatterns = [
    path('weathers/', WeatherListCreateAPIView.as_view(), name='weather-list-create'),
]
