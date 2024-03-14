from django.db import models
from django.contrib.auth.models import User

# # Create your models here.



class Profile(models.Model):
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="instructor"
    )
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    laguages_spoken = models.TextField()
    ability = models.CharField(max_length=50)
    about_me = models.TextField()
    created_on = models. DateTimeField(auto_now_add=True)