from django.urls import path
from weather.apis import WeatherListCreateAPIView
from weather.views import WeatherListView, WeatherChartListView

urlpatterns = [
    path('v1/weathers/', WeatherListCreateAPIView.as_view(), name='weather-list-create'),
    path('weathers/', WeatherListView.as_view(), name='weather-list'),
    path('weathers/chart/', WeatherChartListView.as_view(), name='weather-chart'),
]
