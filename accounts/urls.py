from django.urls import path
from . import views


# create a path or url for REGISTER

urlpatterns = [
    
    path("reg",views.reg,name="reg"),
    path("login",views.Login,name='login'),
    path("logout",views.Logout,name="logout"),
    path("verify_otp",views.verify_otp,name="verify_otp"),
]
