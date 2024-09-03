from django import forms
from django.contrib.auth.models import User
from .models import Booking
# trying something from https://stackoverflow.com/questions/386042/how-to-have-a-link-in-label-of-a-form-field (mrkre's example) 
# Might not be neeeded after all
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


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


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            #'chosen_class',
            # 'class_datetime',
            'waiver_signed',
        ]
        labels = {
            #'chosen_class': 'Class title',
            # 'class_datetime': 'When',
            'waiver_signed': 'By signing up, I agree to Namaste Yoga Studio\'s liability waiver.'
        }


    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Article: https://letscodemore.medium.com/how-to-add-date-input-widget-in-django-forms-50f40aaacb66
        # self.fields['class_date'].widget = forms.widgets.DateInput(
        #     attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'})
        # CHOICES_WHEN = (
        #     ('one', 'one'),
        #     ('two', 'two'),
        #     ('three', 'three'),
        # )
        # self.fields['class_datetime'].widget = forms.widgets.Select(attrs={'choices': CHOICES_WHEN})
        self.fields['waiver_signed'].required = True
        self.fields['waiver_signed'].widget = forms.widgets.CheckboxInput(
            attrs={'type': 'checkbox'})
        #waiver = reverse_lazy("this waiver.")
        #self.fields['waiver_signed'].label = mark_safe(_(
           # "By signing up, I agree to <span>this waiver</span>") % (waiver))


# class DatetimeForm(forms.Form):
#     CHOICES = (
#         ('next', 'next' ),
#         ('second-next', 'second-next' ),
#         ('third-next',  'third-next' )
#     )
#     template = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
