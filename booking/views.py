from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm

def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking received. You will now be redirected to the home page.")
            return redirect('home')  # Redirect to the homepage after successful form submission
    else:
        form = AppointmentForm()
    bookings = Appointment.objects.all()
    return render(request, 'index.html', {'form': form, 'bookings': bookings})

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
            return redirect('home')  # Redirect to the homepage after successful login
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


def index(request):
    booking_success = False  # Initialize booking success flag
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            booking_success = True  # Set booking success flag to True
            messages.success(request, "Booking received.")
            return redirect('home')  # Redirect to the homepage after successful form submission
    else:
        form = AppointmentForm()
    bookings = Appointment.objects.all()
    return render(request, 'index.html', {'form': form, 'bookings': bookings, 'booking_success': booking_success})






