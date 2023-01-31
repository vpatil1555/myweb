from Contact import views
from django.urls import path

urlpatterns = [
   
    path("contact",views.contact,name="contact"),
    path("showdata",views.showdata,name="showdata")
    
]
