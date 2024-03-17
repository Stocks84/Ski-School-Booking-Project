from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('surname', 'languages_spoken')
    search_fields = ['surname']
    list_filter = ('ability', 'created_on')
    summernote_fields = ('about_me',)

# Register your models here.

