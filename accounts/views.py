from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import smtplib
import os
import math
import random
 

# Create your views here.



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        User = auth.authenticate(username=username,password=password)
        
        if User is not None:
            auth.login(request, User)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')    
    

def generate_otp():
    return random.randint(100000, 999999)     


def send_otp(otp, email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('vpatil15550@gmail.com', 'dnmhamqraaasucqj')
    message = f"Your OTP is {otp}"
    server.sendmail('vpatil15550@gmail.com', email, message)
    server.quit()    


def reg(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username already exists')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email taken')
                return redirect('reg')
            
            else:        
                otp = generate_otp()
                send_otp(otp,email)
                return render(request, 'OTP.html')
            
        else:
            messages.warning(request,'password not matching...')
            return redirect('reg')        
    else:
        return render(request,'registration.html')
    
def OTP(request):
    otp = generate_otp()
    first_name = reg(request)
    last_name = reg(request)
    username = reg(request)
    email = reg(request)
    password1 = reg(request)
    user_otp = request.POST['OTP']
    if user_otp == str(otp):
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save();
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('vpatil15550@gmail.com', 'dnmhamqraaasucqj')
        message = f"congratulations {username}\n \n \n \n Registration successful"
        server.sendmail('vpatil15550@gmail.com', email, message)
        server.quit()
        messages.success(request,'user created')
        print("Registration successful!")
        return redirect('login')
    else:
        messages.warning(request,'OTP incorrect!')
        return redirect('reg')
    

def Logout(request):
    auth.logout(request)
    return redirect('/')
     
