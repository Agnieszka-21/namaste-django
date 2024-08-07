from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import  Profile
from .forms import ClientProfileForm


# Create your views here.
def home(request):
    # return HttpResponse('This is the homepage - http response')
    return render(request, 'user_profiles/index.html')


def error404(request):
    return render(request, 'user_profiles/404.html')


@login_required
def profile(request):
    #queryset = Profile.objects.all()
    #current_user = get_object_or_404(queryset, user=user)
    profile_form = ClientProfileForm()
    placeholder_text = "no information"
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'profile_form': profile_form,
        'placeholder_text': placeholder_text,
    }
    return render(request, 'user_profiles/profile.html', context)


# Built based on this: https://docs.djangoproject.com/en/5.0/topics/forms/
@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_form = ClientProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            #return HttpResponseRedirect("/thanks/")
    else:
        profile_form = ClientProfileForm()
    return render(request, 'user_profiles/profile_form.html', {'profile_form': profile_form})