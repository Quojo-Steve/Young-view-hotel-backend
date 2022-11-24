from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('emp_login', views.emp_login),
    path('emp_change_password', views.empchangepassword),
]
