from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


# Code for the following CustomSignupForm has been copied from this article:
# https://www.naukri.com/code360/library/extending-and-customizing-django-allauth
class CustomSignupForm(SignupForm):
    """
    Extends the Allauth signup form
    Adds first and last name (required to sign up)
    """
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ClientProfileForm(forms.ModelForm):
    """
    A ModelForm for the Profile model, used to maintain
    additional information a user might want to store
    in their account
    """
    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'injuries',
            'profile_pic'
        ]
        labels = {
            'date_of_birth': 'Date of birth',
            'injuries': 'Recent or chronic injuries',
            'profile_pic': 'Profile image'
        }

    def __init__(self, *args, **kwargs):
        super(ClientProfileForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = forms.DateInput(
            attrs={'placeholder': 'YYYY-MM-DD'})
