from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Client_User_Profile

# Create your views here.
def home(request):
    # return HttpResponse('This is the homepage - http response')
    return render(request, 'user_profiles/index.html')

@login_required
def profile(request):
    profile = request.user.get_profile()  # or just .profile ?
    return render(request, 'profile.html', {'profile': profile})
    #return HttpResponse("Welcome to Namaste Yoga")
