from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Client_User_Profile

# Create your views here.
@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'user_profiles/profile.html', {'profile': profile})
    # return HttpResponse("Welcome to Namaste Yoga")
