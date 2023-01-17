from django.db import models

# Create your models here.


class enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()
    
