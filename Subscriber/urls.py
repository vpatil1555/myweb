from django.urls import path
from . import views
from Subscriber import views

urlpatterns = [
    path("newsletter", views.newsletter, name="newsletter"),
   
]
