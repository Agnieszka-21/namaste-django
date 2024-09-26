import datetime
from dateutil import parser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils.timezone import make_aware
from django.views import generic
from .forms import UserForm, BookingForm, CancellationForm, BookingUpdateForm
from .models import GroupClass, Booking, SpecificGroupClass
from .models import EventOccurrence, RepeatedEvent
from pytz import timezone


def schedule(request):
    """
    Renders the template for Schedule page

    **Template:**

    :template:`schedule/schedule.html`
    """
    return render(request, 'schedule/schedule.html')


class GroupClassList(generic.ListView):
    """
    Returns all group classes in :model:`schedule.GroupClass`

    **Context**

    ``queryset``
        All  instances of :model:`schedule.GroupClass`

    **Template:**

    :template:`schedule/schedule_list.html`
    """
    queryset = GroupClass.objects.all()
    template_name = 'schedule/schedule_list.html'


class BookingList(generic.ListView):
    """
    Returns all group classes in :model:`schedule.Booking`

    **Context**

    ``queryset``
        All  instances of :model:`schedule.Booking`

    **Template:**

    :template:`schedule/personal_bookings.html`
    """
    queryset = Booking.objects.all()
    template_name = 'schedule/personal_bookings.html'


def schedule_detail(request, id):
    """
    Renders the schedule_detail.html template for
    a chosen group class

    **Context**

    ``queryset``
    All  instances of :model:`schedule.GroupClass`

    ``chosen_class``
    A specific instance of :model:`schedule.GroupClass`

    **Template:**

    :template:`schedule/schedule_detail.html`
    """
    queryset = GroupClass.objects.all()
    chosen_class = get_object_or_404(queryset, id=id)
    default_text = "No information"
    context = {
        'chosen_class': chosen_class,
        'default_text': default_text,
    }
    return render(request, 'schedule/schedule_detail.html', context)


def create_new_specific_class(booking):
    """
    Creates an instance of the specific_group_class
    It is run when user books a class or updates their booking
    and the specific class (on the specific date) does not exist
    in the system
    """
    new_class = SpecificGroupClass.objects.create(
        specific_title=booking.chosen_class.title,
        specific_datetime=booking.class_datetime,
        num_of_participants=1,
    )
    new_class.participants_names.set([booking.client])


def add_participant(existing_class, booking):
    """
    Adds user as a participants in the specific instance of
    specfic_group_class
    The function is run when user books a class or updates their booking
    (chooses a different date for their class)
    It increases num_of_partcipants by 1 and adds the client to the list of
    participants
    """
    existing_class.num_of_participants += 1
    existing_class.participants_names.add(booking.client)
    existing_class.save()


@login_required
def book_class(request, id):
    queryset = GroupClass.objects.all()
    chosen_class = get_object_or_404(queryset, id=id)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user)
        booking_form = BookingForm(data=request.POST)
        context = {'chosen_class': chosen_class, 'user_form': user_form, 'booking_form': booking_form} 
        if user_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.save()
                successful = True
            except:
                messages.error(request, 'ERROR: Oops, something went wrong with your details...')
        if (user_form.is_valid() and successful == True) and booking_form.is_valid():
            try:
                booking = booking_form.save(commit=False)
                booking.chosen_class = chosen_class
                booking.client = request.user
                # Following line of code (string converted into datetime) based on this article:
                # https://www.geeksforgeeks.org/python-convert-string-to-datetime-and-vice-versa/
                booking.class_datetime = make_aware(parser.parse(request.POST['available-dates']))
                clients_active_bookings_qs = Booking.objects.filter(client=booking.client).filter(booking_cancelled=False).filter(class_datetime=booking.class_datetime)
                print('CLIENTS ACTIVE BOOKINGS FOR THAT DATETIME: ', clients_active_bookings_qs)
                chosen_date = request.POST['available-dates']
                try:
                    duplicate = clients_active_bookings_qs.get(chosen_class=booking.chosen_class)
                    print('DUPLICATE: ', duplicate) 
                    messages.info(request, f'You have already booked a place in this class on **{chosen_date}** You can check your classes under **My bookings**')
                    return render(request, 'schedule/book_class.html', context)
                except:
                    booking.save()
                    # When saving a booking, take care of SpecificGroupClass
                    specific_qs = SpecificGroupClass.objects.filter(specific_title=booking.chosen_class.title)
                    print('QS SPECIFIC: ', specific_qs)
                    try:
                        # Check whether the specific class that user is booking already exists in the system. If it does, do the following
                        existing_class = specific_qs.get(specific_datetime=booking.class_datetime)
                        print('EXISTING CLASS: ', existing_class)
                        if existing_class.num_of_participants < 2:
                            add_participant(existing_class, booking)
                        else:
                            booking.booking_cancelled = True
                            booking.cancellation_reason = 'class full'
                            booking.save()
                            messages.error(request, f'This class on **{chosen_date}** is already full. Please choose a different date or go to Schedule and pick a different class.')
                            return render(request, 'schedule/book_class.html', context)
                    except:
                        # If the specific class that the user just booked does not exist in the system yet
                        create_new_specific_class(booking)

                    messages.success(request, f'Your booking for **{booking.chosen_class.title} on {chosen_date}** was successful. See you in the studio!')
                    return redirect('class_schedule')           
            except Exception as e:
                print('ERROR: ', e)
                messages.error(request, 'ERROR: Oops, something went wrong...')
        else:
            print('The form is not valid')
    else:
        user_form = UserForm(instance=request.user)
        booking_form = BookingForm(instance=chosen_class)
        context = {'chosen_class': chosen_class, 'user_form': user_form, 'booking_form': booking_form}
    return render(request, 'schedule/book_class.html', context)


# The following function is based on this article:
# https://towardsdatascience.com/simple-sorting-of-a-list-of-objects-by-a-specific-property-using-python-dac907150394
def sort_future_bookings(future_classes):
    """
    Sorts datetimes of the future_classes, and then 
    sorts client's bookings based on these datetimes

    Used in :view:`personal_bookings`
    """
    sorted_future_class_datetimes = []
    for future_class in future_classes:
        sorted_future_class_datetimes.append(future_class.class_datetime)
    sorted_future_class_datetimes.sort()
    # Sort bookings by the class_datetime attribute
    global sorted_future_classes
    sorted_future_classes = []
    for sorted_datetime in sorted_future_class_datetimes:
        for future_class in future_classes:
            if future_class.class_datetime == sorted_datetime:
                sorted_future_classes.append(future_class)
                break


@login_required
def personal_bookings(request, id):
    """
    Returns a list of a particular client's active bookings for
    upcoming classes, sorted by datetime of these classes

    **Context**

    ``booked_classes``
    Instances of :model:`schedule.Booking` filtered by client

    ``sorted_future_classes``
    A list of a specific client's active bookings for
    upcoming classes, sorted by their datetime

    **Template:**

    :template:`schedule/personal_bookings.html`
    """
    booked_classes = Booking.objects.filter(client=request.user.id)
    # Get current date and time for the specified time zone
    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.astimezone(timezone('Europe/Dublin'))
    # Create a list for future classes booked
    future_classes = []
    for booked_class in booked_classes:
        if (booked_class.class_datetime > current_datetime) and (
            booked_class.booking_cancelled is False):
            future_classes.append(booked_class)
        else:
            past_classes.append(booked_class)
    sort_future_bookings(future_classes)
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'booked_classes': booked_classes,
        'sorted_future_classes': sorted_future_classes
    }
    return render(request, 'schedule/personal_bookings.html', context)


# Function view based on django-render-partial documentation:
# https://pypi.org/project/django-render-partial/
def create_dates(request, *args, **kwargs):
    chosen_class = GroupClass.objects.get(id=kwargs['id'])
    event = RepeatedEvent.objects.create(title=chosen_class)
    first_class = chosen_class.first_class
    weekly = EventOccurrence.objects.create(
        event=event,
        start=first_class,
        end=first_class + (
            datetime.timedelta(minutes=chosen_class.duration_mins)),
        repeat='RRULE:FREQ=WEEKLY')
    # Calculate time
    current_datetime = datetime.datetime.now()
    add_week = datetime.timedelta(days=7)
    one_week_later = current_datetime + add_week
    two_weeks_later = current_datetime + add_week + add_week
    # Create dates/times for the next 3 occurrences of a given group class
    next_class = event.next_occurrence(from_date=current_datetime)
    second_next_class = event.next_occurrence(from_date=one_week_later)
    third_next_class = event.next_occurrence(from_date=two_weeks_later)
    # Create a readable version
    next_class_str = next_class[0]
    second_next_class_str = second_next_class[0]
    third_next_class_str = third_next_class[0]
    kwargs['next_class_str'] = next_class_str
    kwargs['second_next_class_str'] = second_next_class_str
    kwargs['third_next_class_str'] = third_next_class_str
    return render(request, 'schedule/snippets/dates.html', kwargs)


def remove_participant(orig_spec_class, chosen_booking):
    """
    Remove client from the list of participants for their original booked class
    The function is run when client cancels or updates their booking
    It decreases num_of_partcipants by 1 and removes the client from
    the list of participants
    """
    orig_spec_class.num_of_participants -= 1
    orig_spec_class.participants_names.remove(chosen_booking.client)
    orig_spec_class.save()


def handle_cancellation(cancellation_form, chosen_booking, request):
    """
    Mark a booking as cancelled with a specified reason, save changes
    to the booking

    Used in :view:`cancel_booking`
    """
    cancellation = cancellation_form.save(commit=False)
    cancellation.booking_cancelled = True
    cancellation.cancellation_reason = 'client\'s decision'
    cancellation.save()
    # Update details for that specific class
    specific_qs = SpecificGroupClass.objects.filter(
        specific_title=chosen_booking.chosen_class.title)
    orig_spec_class = specific_qs.get(
        specific_datetime=chosen_booking.class_datetime)
    remove_participant(orig_spec_class, chosen_booking)
    messages.success(
        request, f'Your cancellation for **'
        '{chosen_booking.chosen_class.title}** was successful')


@login_required
def cancel_booking(request, id, pk):
    chosen_booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        cancellation_form = CancellationForm(
            data=request.POST, instance=chosen_booking)
        if cancellation_form.is_valid():
            try:
                handle_cancellation(cancellation_form, chosen_booking, request)
                return redirect('my_bookings', request.user.id)
            except Exception:
                messages.error(
                    request, f'Oh no, an error occurred... Please check '
                    '**My bookings** to see if your class was '
                    'successfully cancelled')
        else:
            print('The cancellation form is not valid')
    else:
        cancellation_form = CancellationForm(instance=chosen_booking)
    return render(request, 'schedule/cancel_booking.html', {
        'chosen_booking': chosen_booking,
        'cancellation_form': cancellation_form
        })


def class_full(booking, orig_spec_class, request):
    """
    When a user (client) tries to change their existing
    booking to a class that is already full, revert the change
    to booking.class_datetime, save it, and show a notification
    informing that the class cannot be booked as it's full

    Used in :view:`update_booking`
    """
    booking.class_datetime = orig_spec_class.specific_datetime
    booking.save()
    messages.error(
        request, f'The class on the new date you chose is already full. '
        'Please choose a different date or go to Schedule and pick '
        'a different class.')


@login_required
def update_booking(request, id, pk):
    chosen_booking = Booking.objects.get(id=pk)
    specific_qs = SpecificGroupClass.objects.filter(
        specific_title=chosen_booking.chosen_class.title)
    orig_spec_class = specific_qs.get(
        specific_datetime=chosen_booking.class_datetime)
    if request.method == 'POST':
        booking_update_form = BookingUpdateForm(
            data=request.POST, instance=chosen_booking)
        context = {
            'chosen_booking': chosen_booking,
            'booking_update_form': booking_update_form
        }
        if booking_update_form.is_valid():
            try:
                booking = booking_update_form.save(commit=False)
                booking.class_datetime = make_aware(
                    parser.parse(request.POST['available-dates']))
                clients_active_bookings = Booking.objects.filter(
                    client=chosen_booking.client).filter(
                        booking_cancelled=False).filter(
                            class_datetime=chosen_booking.class_datetime)
                try:
                    # Client already has an active booking for this class
                    duplicate = clients_active_bookings.get(
                        chosen_class=chosen_booking.chosen_class)
                    messages.info(
                        request, f'You have already booked a place '
                        'in this class - please see your classes below')
                    return redirect('my_bookings', request.user.id)
                except Exception:
                    booking.save()
                    # Handle data for specific class (num_of_participants etc.)
                    # Step 1: The new_specific_class already in the system?
                    specific_qs = SpecificGroupClass.objects.filter(
                        specific_title=booking.chosen_class.title)
                    try:
                        # The specific class already exists in the system
                        existing_class = specific_qs.get(
                            specific_datetime=booking.class_datetime)
                        if existing_class.num_of_participants < 2:
                            add_participant(existing_class, booking)
                            remove_participant(orig_spec_class, chosen_booking)
                        else:
                            class_full(booking, orig_spec_class, request)
                            return render(
                                request, 'schedule/edit_booking.html', {
                                    'chosen_booking': chosen_booking,
                                    'booking_update_form': booking_update_form
                                })
                    except Exception:
                        create_new_specific_class(booking)
                        remove_participant(
                            orig_spec_class, chosen_booking)
                    messages.success(
                        request, f'Your update for '
                        f'**{chosen_booking.chosen_class.title}** '
                        'was successful')
                    return redirect('my_bookings', request.user.id)
            except Exception as e:
                print('ERROR', e)
                print('REQUEST: ', request.POST)
        else:
            print('The booking update form is not valid')
    else:
        booking_update_form = BookingUpdateForm(instance=chosen_booking)
    return render(request, 'schedule/edit_booking.html', {
        'chosen_booking': chosen_booking,
        'booking_update_form': booking_update_form
        })
