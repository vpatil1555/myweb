from django.db import models
from django.shortcuts import render
# Create your models here.


class enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()
    
