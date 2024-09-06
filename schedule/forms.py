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

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['email'].disabled = True


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'waiver_signed',
        ]
        labels = {
            'waiver_signed': 'By signing up, I agree to Namaste Yoga Studio\'s liability waiver.'
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['waiver_signed'].required = True
        self.fields['waiver_signed'].widget = forms.widgets.CheckboxInput(
            attrs={'type': 'checkbox'})

