from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Client_User_Profile
from .forms import UserAccountForm

# Create your views here.
def home(request):
    # return HttpResponse('This is the homepage - http response')
    return render(request, 'user_profiles/index.html')

def error404(request):
    return render(request, 'user_profiles/404.html')

@login_required
def profile(request):
    template = loader.get_template('user_profiles/profile.html')
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
    }
    user_account_form = UserAccountForm()
    #return HttpResponse(template.render(context, request))
    return render(request, 'user_profiles/profile.html', context)

    #profile = request.user.get_profile()  # or just .profile ?
    #return HttpResponse("Welcome to Namaste Yoga user account")
    # return render(request, 
    # 'user_profiles/profile.html', {
    #     'context': context,
    #     'user_account_form': user_account_form,
    # })
