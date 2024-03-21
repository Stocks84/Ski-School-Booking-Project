from django.shortcuts import render
from django.views import generic
from .models import Profile
# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    about = Profile.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "profile/profile.html",
        {"profile": profile},
    )