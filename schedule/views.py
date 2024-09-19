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
from .models import GroupClass, Booking, RepeatedEvent, EventOccurrence, SpecificGroupClass
from pytz import timezone



def schedule(request):
    return render(request, 'schedule/schedule.html')


class GroupClassList(generic.ListView):
    queryset = GroupClass.objects.all()

    template_name = 'schedule/schedule_list.html'


class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = 'schedule/personal_bookings.html'


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
        user_form = UserForm(data=request.POST, instance=request.user)
        booking_form = BookingForm(data=request.POST)      
        
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
                try:
                    duplicate = clients_active_bookings_qs.get(chosen_class=booking.chosen_class)
                    print('DUPLICATE: ', duplicate) 
                    messages.info(request, f'You have already booked a place in this class - you can check your classes under **My bookings**')
                    return redirect('/schedule/')
                except:
                    booking.save()
                    # When saving a booking, take care of SpecificGroupClass
                    specific_qs = SpecificGroupClass.objects.filter(specific_title=booking.chosen_class.title)
                    print('QS SPECIFIC: ', specific_qs)
                    try:
                        existing_class = specific_qs.get(specific_datetime=booking.class_datetime)
                        print('EXISTING CLASS: ', existing_class)
                        if existing_class.num_of_participants < 2:
                            existing_class.num_of_participants += 1
                            print('NUM: ', existing_class.num_of_participants)
                            existing_class.participants_names.add(booking.client)
                            existing_class.save()
                        else:
                            booking.booking_cancelled = True
                            booking.cancellation_reason = 'class full'
                            booking.save()
                            messages.error(request, f'This class is already full. Please choose a different date or go to Schedule and pick a different class.')
                            return render(request, 'schedule/book_class.html', {'chosen_class': chosen_class, 'user_form': user_form, 'booking_form': booking_form})
                    except:
                        new_class = SpecificGroupClass.objects.create(
                            specific_title = booking.chosen_class.title,
                            specific_datetime = booking.class_datetime,
                            num_of_participants = 1,
                        )
                        new_class.participants_names.set([booking.client])

                    chosen_date = request.POST['available-dates']
                    messages.success(request, f'Your booking for **{booking.chosen_class.title} on {chosen_date}** was successful. See you in the studio!')
                    return redirect('/schedule/')           

            except Exception as e:
                print('ERROR: ', e)
                # print('REQUEST: ', request.POST)
                messages.error(request, 'ERROR: Oops, something went wrong with your booking...')
        else:
            print('The form is not valid')
    else:
        # Print statement for debugging the function
        print("This is coming from the ELSE in book_class view")
        user_form = UserForm(instance=request.user)
        booking_form = BookingForm(instance=chosen_class)

    # Print statement for debugging the function
    print("About to render template book_class.html")
    return render(request, 'schedule/book_class.html', {'chosen_class': chosen_class, 'user_form': user_form, 'booking_form': booking_form})


@login_required
def personal_bookings(request, id):
    model = Booking
    booked_classes = Booking.objects.filter(client=request.user.id)
    # Get current date and time for the specified time zone
    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.astimezone(timezone('Europe/Dublin'))
    # Create a list for future classes booked, and a list of past classes booked
    future_classes = []
    past_classes = []
    for booked_class in booked_classes:
        if (booked_class.class_datetime > current_datetime) and (booked_class.booking_cancelled == False):
            future_classes.append(booked_class)
        else:
            past_classes.append(booked_class)
    
    # Based on this article:
    # https://towardsdatascience.com/simple-sorting-of-a-list-of-objects-by-a-specific-property-using-python-dac907150394
    # Sort the class_datetime attribute for each of these 2 lists
    sorted_future_class_datetimes = []
    for future_class in future_classes:
        sorted_future_class_datetimes.append(future_class.class_datetime)
    sorted_future_class_datetimes.sort()

    # sorted_past_class_datetimes = []
    # for past_class in past_classes:
    #     sorted_past_class_datetimes.append(future_class.class_datetime)
    # sorted_past_class_datetimes.sort(reverse=True)
    # Sort the list of future classes by class_datetime, in descending order
    sorted_future_classes = []
    for sorted_datetime in sorted_future_class_datetimes:
        for future_class in future_classes:
            if future_class.class_datetime == sorted_datetime:
                sorted_future_classes.append(future_class)
                break
    # Sort the list of past classes by class_datetime, in descending order
    # sorted_past_classes = []
    # for sorted_datetime in sorted_past_class_datetimes:
    #     for past_class in past_classes:
    #         if past_class.class_datetime == sorted_datetime:
    #             sorted_past_classes.append(past_class)
    #             break

    # Pagination article: 
    # https://realpython.com/django-pagination/#using-the-django-paginator-in-views
    # p = Paginator(sorted_future_classes, 2)
    # print(p.count)
    # print(p.num_pages)
    # page1 = p.page(1)
    # page2 = p.page(2)
    # page3 = p.page(3)
    # print(page1)
    # page = p.page(request.GET.get('page'))
    #chosen_booking = 
    # for sfc in sorted_future_classes:
    #     print(sfc.pk)
    default_text = "No information"
    context = {
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'default_text': default_text,
        'booked_classes': booked_classes,
        'sorted_future_classes': sorted_future_classes,
        # 'sorted_past_classes': sorted_past_classes,
        # 'page_obj': page1,
        # 'page_obj': page2,
        # 'page_obj': page3,
    }

    return render(request, 'schedule/personal_bookings.html', context)


# Function view based on django-render-partial documentation: https://pypi.org/project/django-render-partial/
def create_dates(request, *args, **kwargs):
    chosen_class = GroupClass.objects.get(id=kwargs['id'])
    event = RepeatedEvent.objects.create(title=chosen_class)
    first_class = chosen_class.first_class
    weekly = EventOccurrence.objects.create(
        event=event,
        start=first_class,
        end=first_class + (datetime.timedelta(minutes=chosen_class.duration_mins)),
        repeat='RRULE:FREQ=WEEKLY')

    current_datetime = datetime.datetime.now()
    print('CURENT DATETIME: ', current_datetime)
    add_week = datetime.timedelta(days=7)
    one_week_later = current_datetime + add_week
    two_weeks_later = current_datetime + add_week + add_week

    next_class = event.next_occurrence(from_date=current_datetime)
    second_next_class = event.next_occurrence(from_date=one_week_later)
    third_next_class = event.next_occurrence(from_date=two_weeks_later)

    next_class_str = next_class[0]
    second_next_class_str = second_next_class[0]
    third_next_class_str = third_next_class[0]
    kwargs['next_class_str'] = next_class_str
    kwargs['second_next_class_str'] = second_next_class_str
    kwargs['third_next_class_str'] = third_next_class_str

    return render(request, 'schedule/snippets/dates.html', kwargs)


@login_required
def cancel_booking(request, id, pk):
    chosen_booking = Booking.objects.get(id=pk)
    print('CHOSEN BOOKING: ', chosen_booking)
    
    if request.method == 'POST':
        # Print statement for debugging the function
        print("Received a POST request for a booking cancellation")
        cancellation_form = CancellationForm(data=request.POST, instance=chosen_booking)

        if cancellation_form.is_valid():
            try:
                cancellation = cancellation_form.save(commit=False)
                cancellation.booking_cancelled = True
                cancellation.cancellation_reason = 'client\'s decision'
                cancellation.save()
                # Update num_of_participants and the list of participants_names for that specific class
                specific_qs = SpecificGroupClass.objects.filter(specific_title=chosen_booking.chosen_class.title)
                existing_class = specific_qs.get(specific_datetime=chosen_booking.class_datetime)
                existing_class.num_of_participants -= 1
                existing_class.participants_names.remove(chosen_booking.client)
                existing_class.save()
                messages.success(request, f'Your cancellation for **{chosen_booking.chosen_class.title}** was successful')
                return redirect('/schedule/')
            except Exception as e:
                print('ERROR', e)
                print('REQUEST: ', request.POST)
        else:
            print('The cancellation form is not valid')
    else:
        cancellation_form = CancellationForm(instance=chosen_booking)

    return render(request, 'schedule/cancel_booking.html', {'chosen_booking': chosen_booking, 'cancellation_form': cancellation_form})


@login_required
def update_booking(request, id, pk):
    chosen_booking = Booking.objects.get(id=pk)
    print('CHOSEN BOOKING: ', chosen_booking)

    if request.method == 'POST':
        # Print statement for debugging the function
        print("Received a POST request for a booking update")
        booking_update_form = BookingUpdateForm(data=request.POST, instance=chosen_booking)

        if booking_update_form.is_valid():
            try:
                update = booking_update_form.save(commit=False)
                update.class_datetime = make_aware(parser.parse(request.POST['available-dates']))
                clients_active_bookings = Booking.objects.filter(client=chosen_booking.client).filter(booking_cancelled=False).filter(class_datetime=chosen_booking.class_datetime)
                print('CLIENTS ACTIVE BOOKINGS FOR THAT DATETIME: ', clients_active_bookings)
                try:
                    duplicate = clients_active_bookings.get(chosen_class=chosen_booking.chosen_class)
                    print('DUPLICATE: ', duplicate)
                    messages.info(request, f'You have already booked a place in this class - you can check your classes under **My bookings**')
                    return redirect('/schedule/')
                except:
                    update.save()
                    messages.success(request, f'Your update for **{chosen_booking.chosen_class.title}** was successful')
                    return redirect('/schedule/')
            except Exception as e:
                print('ERROR', e)
                print('REQUEST: ', request.POST)
        else:
            print('The booking update form is not valid')
    else:
        booking_update_form = BookingUpdateForm(instance=chosen_booking)
    return render(request, 'schedule/edit_booking.html', {'chosen_booking': chosen_booking, 'booking_update_form': booking_update_form})
