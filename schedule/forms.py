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


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'chosen_class',
            'class_date',
        ]
        labels = {
            'chosen_class': 'Class title',
            'class_date': 'When',
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Article: https://letscodemore.medium.com/how-to-add-date-input-widget-in-django-forms-50f40aaacb66
        self.fields['class_date'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'})
