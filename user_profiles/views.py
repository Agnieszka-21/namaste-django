from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import ClientProfileForm
from .models import Profile


def home(request):
    """
    Renders a custom template used for the homepage

    **Template:**

    :template:`user_profiles/index.html`
    """
    return render(request, 'user_profiles/index.html')


def error404(request):
    """
    Renders a custom template when error 404 occurs

    **Template:**

    :template:`404.html`
    """
    return render(request, '404.html')


def error500(request):
    """
    Renders a custom template when error 500 occurs

    **Template:**

    :template:`500.html`
    """
    return render(request, '500.html')


class ProfileList(generic.ListView):
    """
    Returns all profiles in :model:`user_profiles.Profile`

    **Context**

    ``queryset``
        All  instances of :model:`user_profiles.Profile`

    **Template:**

    :template:`base.html`
    """
    queryset = Profile.objects.all()
    template_name = "base.html"


@login_required
def profile(request, id):
    """
    Returns a specific object in :model:`user_profiles.Profile`
    - a logged-in user's profile information

    **Context**

    ``name``
    The full name of the logged-in user

    ``email``
    The email address of the logged-in user

    ``current_user``
    The specific logged-in user

    ``default_text``
    A default string, used in the related template when
    no information has been saved

    **Template:**

    :template:`user_profiles/profile.html`
    """
    current_user = Profile.objects.get(user=request.user.id)
    default_text = "No information"
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'current_user': current_user,
        'default_text': default_text,
    }
    return render(request, 'user_profiles/profile.html', context)


@login_required
def editProfile(request, id):
    """
    Returns a specific object in :model:`user_profiles.Profile`
    - a logged-in user's profile information

    **Context**

    ``profile_form``
    The ClientProfileForm used to maintain additional
    data a logged in user might want to store in their account

    ``current_user``
    The specific logged-in user

    **Template:**

    :template:`user_profiles/profile_form.html`
    """
    current_user = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        profile_form = ClientProfileForm(
            request.POST, request.FILES, instance=current_user)
        if profile_form.is_valid():
            try:
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, 'Your profile has been updated')
            except Exception:
                messages.error(request, 'Oops, something went wrong...')
            return redirect('profile', request.user.id)
    else:
        profile_form = ClientProfileForm(instance=current_user)
    return render(request, 'user_profiles/profile_form.html', {
        'profile_form': profile_form, 'current_user': current_user})
