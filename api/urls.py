from django.urls import path
from rest_framework import routers
from api import api_views

urlpatterns = [
<<<<<<< HEAD
    path('salaries', api_views.SalariesAPIView.as_view(), name='salaries')    
=======
    path('salaries', api_views.SalariesAPIView.as_view(), name='salaries')
>>>>>>> 2ae3606cff64698c277fb1c11ebc80dbae1fad17
]