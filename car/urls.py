from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('addCars',views.AddCarView.as_view(),name='addCars'),
# path('profile/',views.profile,name='profile')

    
]