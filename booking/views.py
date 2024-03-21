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

class appoinment_detail(generic.ListView):
    queryset = Appointment.objects.all()
    template_name = "booking/appointment_detail.html"
    
    def appointment_detail(request):
        """
        Display an individual booking
        """

        queryset = Appointment.objects.all(surname)
        appointment = get_object_or_404(queryset)

        return render(
            request,
            "booking/appoinment_detail.html",
            {"appointment": appointment},
        )






