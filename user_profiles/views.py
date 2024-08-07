from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse
from .models import  Profile
from .forms import ClientProfileForm


# Create your views here.
def home(request):
    # return HttpResponse('This is the homepage - http response')
    return render(request, 'user_profiles/index.html')


def error404(request):
    return render(request, 'user_profiles/404.html')


class ProfileList(generic.ListView):
    """
    Returns all profiles in :model:`user_profile.Profile`
    **Context**

    ``queryset``
        All  instances of :model:`user_profile.Post`

    **Template:**

    :template:`base.html`
    """
    queryset = Profile.objects.all()
    template_name = "base.html"


@login_required
def profile(request, id):
    queryset = Profile.objects.all()
    current_user = get_object_or_404(queryset, user=id)
    default_text = "No information"
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'current_user': current_user,
        'default_text': default_text,
    }
    return render(request, 'user_profiles/profile.html', context)


# Built based on this: https://docs.djangoproject.com/en/5.0/topics/forms/
@login_required
def editProfile(request, id):
    queryset = Profile.objects.all()
    current_user = get_object_or_404(queryset, user=request.user)
    if request.method == 'POST':
        profile_form = ClientProfileForm(request.POST, request.FILES, instance=current_user)
        if profile_form.is_valid():
            try:
                profile_form.save()
                messages.success(request, 'Your profile has been updated')
                return redirect(profile, request.user.id)
            except:
                messages.error(request, 'ERROR: Oops, something went wrong...')
    else:
        profile_form = ClientProfileForm(instance=current_user)
    return render(request, 'user_profiles/profile_form.html', {'profile_form': profile_form})