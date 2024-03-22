from . import views
from django.urls import path
from .views import login_view, signup_view, logout_view

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    # path('booking/', views.AppointmentList.as_view(), name='booking-urls'),
    # path('appointment/', views.appointment_detail.as_view(), name='appointment-detail'),
    ]