from django.urls import path
from rest_framework import routers
from api import api_views

urlpatterns = [
    path('salaries', api_views.SalariesAPIView.as_view(), name='salaries')
]