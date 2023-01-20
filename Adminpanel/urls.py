from django.contrib import admin
from django.urls import path
from .views import *
from Adminpanel import views

urlpatterns = [
    path("",views.admin_login,name="admin_login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("admin_logout",views.admin_logout,name="admin_logout"),
    path("user",views.user,name="user")
]
