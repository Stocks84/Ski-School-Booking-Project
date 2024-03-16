from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('surname', 'meeting_point')
    search_fields = ['surname']
    list_filter = ('meeting_point',)
    summernote_fields = ('special_reuirements',)
# Register your models here.

