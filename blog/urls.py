from django.urls import path

from . import views

# create a path or url

urlpatterns = [
    
    path("",views.index,name='home'),
    path("callback",views.callback,name="callback"),
    path("index",views.index,name="home"),
    path("about",views.about,name="about"),
    path("what_we_do",views.what_we_do,name="what_we_do"),
    path("testimonial",views.testimonial,name="testimonial"),
    
] 
