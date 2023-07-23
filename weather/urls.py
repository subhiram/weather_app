from django.urls import path
from weather import views

urlpatterns = [
    path('', views.get_city, name='city_input'),
    path('city_two/', views.city, name='city')
]