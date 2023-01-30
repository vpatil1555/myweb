from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import smtplib
import os
import math
import random
from django.utils import timezone
from datetime import timedelta
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


def send_otp(email):
    otp = random.randint(100000, 999999)
    #user =  User.objects.get(email=email)
    #OTP.objects.create(user=user,otp=otp)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('vpatil15550@gmail.com', 'dnmhamqraaasucqj')
    message = f"Your OTP is {otp}"
    server.sendmail('vpatil15550@gmail.com', email, message)
    server.quit()   
    return otp 

  
    
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
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                print()
                otp = send_otp(email)
                request.session['otp'] = otp
                print("otp sent")
                return redirect('verify_otp')
        else:
            messages.warning(request,'password not matching...')
            return redirect('reg')        
    else:
        return render(request,'registration.html')



    
def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('OTP')
        session_otp = request.session.get('otp')
        if otp == session_otp:
            user = User.objects.get(email=request.session.get('email'))
            user.is_verified = True
            user.save()
            print("saved")
            return render(request, 'login.html')
        else:
            return render(request, 'OTP.html',  {'error': 'invalid otp'})
    else:
        return render(request, 'OTP.html')
            
            
def Logout(request):
    auth.logout(request)
    return redirect('/')
     
