from django.shortcuts import render
from Subscriber.models import subscriber
import smtplib

# Create your views here.
def newsletter(request):
    if request.method == 'POST':
        subscriber_name = request.POST['yourname']
        subscriber_email = request.POST['subscriber']
    
    news = subscriber(NAME=subscriber_name,EMAIL=subscriber_email)
    news.save()
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()


    server.login('vpatil15550@gmail.com', 'dnmhamqraaasucqj')
    
    server.sendmail('vpatil15550@gmail.com', subscriber_email, f'Hi, {subscriber_name}\n \n \n \n \n \n Thank you for subscribing from now on get our latest updates and news on the go\n \n \n \n \n \n  Thank You.')
    print(f'{subscriber_name }you have subscribed thank you')
    
    return render(request, 'index.html')  