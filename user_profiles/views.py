from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Client_User_Profile
from .forms import ClientProfileForm

# Create your views here.
def home(request):
    # return HttpResponse('This is the homepage - http response')
    return render(request, 'user_profiles/index.html')

def error404(request):
    return render(request, 'user_profiles/404.html')


@login_required
def profile(request):
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
    }
    return render(request, 'user_profiles/profile.html', context)


# Built based on this: https://docs.djangoproject.com/en/5.0/topics/forms/
@login_required
def editProfile(request):
    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = ClientProfileForm()
    return render(request, 'user_profiles/profile_form.html', {'form': form})