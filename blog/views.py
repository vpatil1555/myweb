from django.shortcuts import render
  #import the class from models
from Contact.models import enquiry
from Designs.models import design

# Create your views here.

# create a function to request from http

def index(request):
    
    dests = design.objects.all()
    
    return render(request, "index.html",  {'types': dests})


def callback(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone_no']
        email = request.POST['email']
        message = request.POST['message']
        
        data = enquiry(name=name,phone=phone,email=email,message=message)
        data.save()
        print("this is post")
        
    return render(request, 'callback.html')


   

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def what_we_do(request):
    return render(request, 'what_we_do.html')

def testimonial(request):
    return render(request, 'testimonial.html')



        
    