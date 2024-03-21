from django.shortcuts import render
from django.views import generic
from .models import Appointment
# Create your views here.

class Home(generic.ListView):
    queryset = Appointment()
    template_name = "booking/index.html"

class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all().order_by("-created_on")
    template_name = "booking/booking.html"
    paginate_by = 4






