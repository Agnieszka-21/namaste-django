from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import GroupClass
# from .models import Client_User_Profile

# Create your views here.
def schedule(request):
    return render(request, 'schedule/schedule.html')
    #return HttpResponse('This is the schedule page')


class GroupClassList(generic.ListView):
    queryset = GroupClass.objects.all()
    template_name = 'schedule/schedule_list.html'
