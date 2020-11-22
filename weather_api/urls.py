from django.urls import path
from .views import weather_city


urlpatterns = [
    path('api/v1/weather/', weather_city, name='weather'),
]