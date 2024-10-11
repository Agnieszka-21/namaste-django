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

    def test_first_name_is_required(self):
        """
        Tests whether the field 'first_name' is required
        """
        form = CustomSignupForm()
        self.assertTrue(form.fields['first_name'].required)

    def test_last_name_is_required(self):
        """
        Tests whether the field 'first_name' is required
        """
        form = CustomSignupForm()
        self.assertTrue(form.fields['last_name'].required)


class ClientProfileFormTest(SimpleTestCase):

    def test_dob_field_label(self):
        """
        Tests the label of the field 'date_of_birth'
        """
        form = ClientProfileForm()
        self.assertTrue(
            form.fields['date_of_birth'].label == 'Date of birth')

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

    def test_dob_is_not_required(self):
        """
        Tests whether the field 'date_of_birth' is not required
        """
        form = ClientProfileForm()
        self.assertFalse(form.fields['date_of_birth'].required)

    def test_injuries_is_not_required(self):
        """
        Tests whether the field 'injuries' is not required
        """
        form = ClientProfileForm()
        self.assertFalse(form.fields['injuries'].required)

    def test_profile_pic_is_not_required(self):
        """
        Tests whether the field 'profile_pic' is not required
        """
        form = ClientProfileForm()
        self.assertFalse(form.fields['profile_pic'].required)

    def test_dob_placeholder(self):
        """
        Test input type and placeholder value for the
        'date_of_birth' field
        """
        form = ClientProfileForm()
        self.assertEqual(
            form.fields['date_of_birth'].widget.__class__.__name__,
            'DateInput')
        self.assertEqual(
            form.fields['date_of_birth'].widget.attrs['placeholder'],
            'YYYY-MM-DD')
