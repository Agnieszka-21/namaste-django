from django.test import TestCase
from ..forms import CustomSignupForm, ClientProfileForm


class CustomSignupFormTest(TestCase):
    """
    Tests the following parameters of each custom form field:
    max_length, and label
    """
    def test_first_name_max_length(self):
        form = CustomSignupForm()
        self.assertEqual(form.fields['first_name'].max_length, 25)

    def test_last_name_max_length(self):
        form = CustomSignupForm()
        self.assertEqual(form.fields['last_name'].max_length, 25)

    def test_first_name_field_label(self):
        form = CustomSignupForm()
        self.assertTrue(form.fields['first_name'].label == 'First Name')

    def test_last_name_field_label(self):
        form = CustomSignupForm()
        self.assertTrue(form.fields['last_name'].label == 'Last Name')


class ClientProfileFormTest(TestCase):
    """
    Tests the labels of customized form fields
    """
    def test_injuries_field_label(self):
        form = ClientProfileForm()
        self.assertTrue(
            form.fields['injuries'].label == 'Recent or chronic injuries')

    def test_profile_pic_field_label(self):
        form = ClientProfileForm()
        self.assertTrue(form.fields['profile_pic'].label == 'Profile image')
