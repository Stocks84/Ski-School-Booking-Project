from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def instructor_me(request):
    return HttpResponse("This is the instructor page")