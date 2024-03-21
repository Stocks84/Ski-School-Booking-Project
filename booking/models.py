from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Confirmed"))
# Create your models here.


class Appointment(models.Model):
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="members"
    )
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.IntegerField(unique=True)
    date_and_time = models.DateTimeField(auto_now=False)
    meeting_point = models.CharField(max_length=200)
    special_requirements = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Booked_on:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.first_name} {self.surname}"
