from django.test import SimpleTestCase
from ..forms import UserForm, BookingForm


class UserFormTest(SimpleTestCase):

    def test_first_name_is_required(self):
        """
        Tests whether the field 'first_name' is required
        """
        form = UserForm()
        self.assertTrue(form.fields['first_name'].required)

    def test_last_name_is_required(self):
        """
        Tests whether the field 'last_name' is required
        """
        form = UserForm()
        self.assertTrue(form.fields['last_name'].required)

    def test_email_is_required(self):
        """
        Tests whether the field 'email' is required
        """
        form = UserForm()
        self.assertTrue(form.fields['email'].required)

    def test_first_name_is_uneditable(self):
        """
        Tests whether the field 'first_name' is uneditable
        """
        form = UserForm()
        self.assertTrue(form.fields['first_name'].disabled)

    def test_last_name_is_uneditable(self):
        """
        Tests whether the field 'last_name' is uneditable
        """
        form = UserForm()
        self.assertTrue(form.fields['last_name'].disabled)

    def test_email_is_uneditable(self):
        """
        Tests whether the field 'email' is uneditable
        """
        form = UserForm()
        self.assertTrue(form.fields['email'].disabled)


class BookingFormTest(SimpleTestCase):

    def test_waiver_signed_field_label(self):
        """
        Tests the label of the field 'waiver_signed'
        """
        form = BookingForm()
        self.assertTrue(
            form.fields['waiver_signed'].label == 'By signing up, '
            'I agree to Namaste Yoga Studio\'s liability waiver.')

    def test_waiver_signed_is_required(self):
        """
        Tests whether the field 'waiver_signed' is required
        """
        form = BookingForm()
        self.assertTrue(form.fields['waiver_signed'].required)

    def test_waiver_signed_is_a_checkbox(self):
        """
        Tests whether the field 'waiver_signed' is a checkbox
        """
        form = BookingForm()
        self.assertEqual(
            form.fields['waiver_signed'].widget.__class__.__name__,
            'CheckboxInput')

    def test_booking_form_is_valid(self):
        """
        Tests whether the field 'waiver_signed' is True,
        therefore making the form valid
        """
        form = BookingForm()
        checked = form.fields['waiver_signed'] is True
        updated_form = BookingForm(data={'waiver_signed': checked})
        self.assertTrue(updated_form.is_valid())
