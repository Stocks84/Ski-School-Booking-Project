from django.shortcuts import render
from django.views import generic
from .models import Appointment
# Create your views here.

class AppointmentList(generic.ListView):
    model = Appointment



