from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout)
]