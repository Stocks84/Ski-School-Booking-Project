from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    First_name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Email_address = models.EmailField(max_length=100, unique=True)
    Phone_number = models.IntegerField(unique=True)
    Date_and_time = models.DateTimeField(auto_now=False)
    Meeting_point = models.CharField(max_length=200)
    Special_requirements = models.CharField(max_length=200)
