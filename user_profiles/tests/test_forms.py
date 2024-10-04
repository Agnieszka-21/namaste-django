from django.test import SimpleTestCase
from ..forms import CustomSignupForm, ClientProfileForm


class CustomSignupFormTest(SimpleTestCase):

    def test_first_name_max_length(self):
        """
        Tests the maximum length of the field 'first_name'
        """
        form = CustomSignupForm()
        self.assertEqual(form.fields['first_name'].max_length, 25)

    def test_last_name_max_length(self):
        """
        Tests the maximum length of the field 'last_name'
        """
        form = CustomSignupForm()
        self.assertEqual(form.fields['last_name'].max_length, 25)

    def test_first_name_field_label(self):
        """
        Tests the label of the field 'first_name'
        """
        form = CustomSignupForm()
        self.assertTrue(form.fields['first_name'].label == 'First Name')

    def test_last_name_field_label(self):
        """
        Tests the label of the field 'last_name'
        """
        form = CustomSignupForm()
        self.assertTrue(form.fields['last_name'].label == 'Last Name')


class ClientProfileFormTest(SimpleTestCase):
    
    def test_injuries_field_label(self):
        """
        Tests the label of the field 'injuries'
        """
        form = ClientProfileForm()
        self.assertTrue(
            form.fields['injuries'].label == 'Recent or chronic injuries')

    def test_profile_pic_field_label(self):
        """
        Tests the label of the field 'profile_pic'
        """
        form = ClientProfileForm()
        self.assertTrue(form.fields['profile_pic'].label == 'Profile image')
