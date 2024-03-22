from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('member','first_name', 'surname', 'email_address', 'phone_number', 'meeting_point', 'special_requirements')
