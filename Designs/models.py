from django.db import models


# Create your models here.

# create a class with variables
# convert class to models


class design(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')