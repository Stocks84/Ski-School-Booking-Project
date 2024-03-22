from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import Appointment
# Create your views here.


def index(request):
    bookings = Appointment.objects.all()
    return render(request, 'index.html', {'bookings': bookings})


def login_view(request):
    """
    Members Log in
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

def signup_view(request):
    """
    Members sign up
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# class Home(generic.ListView):
#     queryset = Appointment()
#     template_name = "booking/index.html"

# class AppointmentList(generic.ListView):
#     queryset = Appointment.objects.all().order_by("-created_on")
#     template_name = "booking/booking.html"
#     paginate_by = 4

# class appointment_detail(generic.ListView):
#     queryset = Appointment.objects.all()
#     template_name = "booking/appointment_detail.html"
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






