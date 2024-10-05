from django import forms
from django.contrib.auth.models import User
from .models import Booking


class UserForm(forms.ModelForm):
    """
    A ModelForm for the User model

    Applied in the book_class view to display
    the logged-in user's data
    """
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['email'].disabled = True


class BookingForm(forms.ModelForm):
    """
    A ModelForm for the Booking model

    Applied in the book_class view to ensure that
    user signs the liability waiver
    """
    class Meta:
        model = Booking
        fields = [
            'waiver_signed',
        ]
        labels = {
            'waiver_signed': 'By signing up, I agree to '
            'Namaste Yoga Studio\'s liability waiver.'
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['waiver_signed'].required = True
        self.fields['waiver_signed'].widget = forms.widgets.CheckboxInput(
            attrs={'type': 'checkbox'})


class CancellationForm(forms.ModelForm):
    """
    A ModelForm for the Booking model

    Applied in the cancel_booking view
    """
    class Meta:
        model = Booking
        fields = [
            'booking_cancelled',
        ]


class BookingUpdateForm(forms.ModelForm):
    """
    A ModelForm for the Booking model

    Applied in the update_booking view to save the new datetime
    the user has chosen for their booked class
    """
    class Meta:
        model = Booking
        fields = [
            'class_datetime',
        ]
