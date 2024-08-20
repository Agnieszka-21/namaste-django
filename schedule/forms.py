from django import forms
from django.contrib.auth.models import User
from .models import Booking


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'chosen_class',
        ]
        labels = {
            'chosen_class': 'Class title',
        }

        # def __init__(self, *args, **kwargs):
        #     super(BookingForm, self).__init__(*args, **kwargs)
