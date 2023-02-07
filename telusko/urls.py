"""telusko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from Contact import views as view
from Subscriber import views as ss
from Adminpanel import views as ap


urlpatterns = [
    path("", include('blog.urls')),
    path("Adminpanel/admin_login",include('Adminpanel.urls')),
    path("admin_logout",ap.admin_logout,name="admin_logout"),
    path("Adminpanel/dashboard",ap.dashboard,name="dashboard"),
    path("user",ap.user,name="user"),
    path("dashboard",ap.dashboard,name="dashboard"),
    path("Enquirys",ap.Enquirys,name="Enquirys"),
    path("Subscribers",ap.Subscribers,name="Subscribers"),
    path('dj-admin/', admin.site.urls),
    path("blog/",include('blog.urls')),
    path("accounts/",include('accounts.urls')),
    path("accounts/Login",views.Login,name="login"),
    path("accounts/Logout",views.Logout,name="logout"),
    path("accounts/reg",views.reg,name="reg"),
    path("accounts/verify_otp",views.verify_otp,name="verify_otp"),
    path("contact",view.contact,name="contact"),
    path("newsletter",ss.newsletter,name="newsletter")
    ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)