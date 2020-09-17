from django.urls import path
from .views import Today_Weather
urlpatterns = [
    path('check_weather/',Today_Weather.as_view()),
]