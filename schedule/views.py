from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import GroupClass, Booking
from .forms import UserForm, BookingForm
from django.contrib.auth.models import User


# Create your views here.
def schedule(request):
    return render(request, 'schedule/schedule.html')
    #return HttpResponse('This is the schedule page')


class GroupClassList(generic.ListView):
    queryset = GroupClass.objects.all()
    template_name = 'schedule/schedule_list.html'


def schedule_detail(request, id):
    queryset = GroupClass.objects.all()
    chosen_class = get_object_or_404(queryset, id=id)
    default_text = "No information"
    context = {
        'chosen_class': chosen_class,
        'default_text': default_text,
    }
    return render(request, 'schedule/schedule_detail.html', context)



@login_required
def book_class(request, id):
    queryset = GroupClass.objects.all()
    chosen_class = get_object_or_404(queryset, id=id)

    # Print statement for debugging the function
    print(chosen_class)
    if request.method == 'POST':
        # Print statement for debugging the function
        print("Received a POST request")
        # successful = False
        user_form = UserForm(data=request.POST, instance=request.user)
        booking_form = BookingForm(data=request.POST)      
        
        if user_form.is_valid():
            try:
                user = user_form.save(commit=False)
                #user.username = request.user  ??? not sure about this
                user.save()
                messages.success(request, 'Your details have been saved') # remove this message? Doesn't seem necessary
                successful = True
                #return redirect('schedule', request.user.id)
            except:
                messages.error(request, 'ERROR: Oops, something went wrong with your details...')
        if (user_form.is_valid() and successful == True) and booking_form.is_valid():
            try:
                booking = booking_form.save(commit=False)
                booking.chosen_class = chosen_class
                booking.client = request.user
                booking.save()
                print(f'Chosen class: {booking.chosen_class}')
                print(f'Client is {booking.client}')
                messages.success(request, f'Your booking for **{booking.chosen_class}** was successful. See you in the studio!')
                return redirect('/schedule/')
            except:
                messages.error(request, 'ERROR: Oops, something went wrong with your booking...')
        else:
            print('The user form has not been saved successfully')
    else:
        # Print statement for debugging the function
        print("This is coming from the ELSE in book_class view")
        user_form = UserForm(instance=request.user)
        booking_form = BookingForm(instance=chosen_class)
        
    # Print statement for debugging the function
    print("About to render template book_class.html")
    return render(request, 'schedule/book_class.html', {'chosen_class': chosen_class, 'user_form': user_form, 'booking_form': booking_form})


# Optional Tutorial: https://github.com/mchesler613/django_adventures/blob/main/multi-modelforms_in_template.md



@login_required
def personal_bookings(request, id):
    model = Booking
    booked_classes = Booking.objects.filter(client=request.user.id)
    print(booked_classes)
    default_text = "No information"
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'default_text': default_text,
        'booked_classes': booked_classes,
    }
    return render(request, 'schedule/personal_bookings.html', context)
