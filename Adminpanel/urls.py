from django.contrib import admin
from django.urls import path
from .views import *
from Adminpanel import views

urlpatterns = [
    path("",views.admin_login,name="admin_login"),
    path("dashboard",views.dashboard,name="dashboard")
]
