from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'chosen_class',
            'class_date',
            'client',
        ]
        labels = {
            'chosen_class': 'Class title',
            'class date': 'Class date',
            'client': 'Full name',
        }

        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
