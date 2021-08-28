from django.contrib import admin
from django.urls import path, include
from . import views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.wall, name = 'wall'),
    path('update/<str:pk>/', views.update, name = 'update'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
    path('register/', users_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'), 
]
