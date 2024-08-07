from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


# https://www.naukri.com/code360/library/extending-and-customizing-django-allauth
# https://stackoverflow.com/questions/70809519/how-do-i-customize-django-allauth-sign-up-forms-to-look-the-way-i-want  
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'injuries',
            'signed_waiver',
            'profile_pic',
        ]

        def __init__(self, *args, **kwargs):
            super(ClientProfileForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})
