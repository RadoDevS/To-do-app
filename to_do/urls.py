from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wall, name = 'wall'),
    path('add/', views.add, name = 'add')
]
