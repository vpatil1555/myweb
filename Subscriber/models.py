from django.db import models

# Create your models here.

class subscriber(models.Model):
    NAME = models.CharField( max_length=50) 
    EMAIL = models.EmailField()