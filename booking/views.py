from django.shortcuts import render, get_object_or_404
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

class appointment_detail(generic.ListView):
    queryset = Appointment.objects.all()
    template_name = "booking/appointment_detail.html"
# def appointment_detail(request, email_address):
#     """
#     Display an individual profile

#     """

#     queryset = Appointment.objects.filter(status=1)
#     post = get_object_or_404(queryset, email_address=email_address)

#     return render(
#         request,
#         "booking/appointment_detail.html",
#         {"appoinment": appointment},
#     )






