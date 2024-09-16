from allauth.account.forms import SignupForm
from cloudinary.forms import CloudinaryFileField
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
            'profile_pic'
        ]
        labels = {
            'date_of_birth': 'Date of birth',
            'injuries': 'Recent or chronic injuries',
            'profile_pic': 'Profile image'
        }
        #profile_pic = CloudinaryFileField()

        # def __init__(self, *args, **kwargs):
        #     super(ClientProfileForm, self).__init__(*args, **kwargs)
        #     self.fields['profile_pic'].required=False
            

