# https://www.naukri.com/code360/library/extending-and-customizing-django-allauth
# https://stackoverflow.com/questions/70809519/how-do-i-customize-django-allauth-sign-up-forms-to-look-the-way-i-want  

from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user