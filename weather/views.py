from django.utils import timezone
from django.views.generic.list import ListView
from weather.models import Weather


class WeatherListView(ListView):
    model = Weather
    paginate_by = 100

    def get_queryset(self):
        return Weather.objects.order_by('-id')


class WeatherChartListView(ListView):
    model = Weather
    paginate_by = 20
    template_name = 'weather/chart.html'

    def get_queryset(self):
        return Weather.objects.order_by('-id')
