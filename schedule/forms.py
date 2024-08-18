from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking