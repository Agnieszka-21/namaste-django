from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'chosen_class',
        ]
        labels = {
            'chosen_class': 'Class title',
        }

        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
