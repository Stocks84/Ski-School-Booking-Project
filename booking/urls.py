from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('booking/', views.AppointmentList.as_view(), name='booking-urls'),
    ]