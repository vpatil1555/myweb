from django.shortcuts import render
from Contact.models import enquiry

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone_no']
        email = request.POST['email']
        message = request.POST['message']
        
        data = enquiry(name=name,phone=phone,email=email,message=message)
        data.save()
        print("this is post")
        
    return render(request, 'index.html')

    
