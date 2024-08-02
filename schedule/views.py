from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from .models import Client_User_Profile

# Create your views here.
def schedule(request):
    # render (request, 'schedule/class_schedule.html')
    return HttpResponse('This is the schedule page')
