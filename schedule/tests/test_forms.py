from django import forms
from django.test import SimpleTestCase
from ..forms import UserForm, BookingForm


class UserFormTest(SimpleTestCase):
    def test_first_name_is_required(self):
        form = UserForm()
        self.assertTrue(form.fields['first_name'].required)

    def test_last_name_is_required(self):
        form = UserForm()
        self.assertTrue(form.fields['last_name'].required)

    def test_email_is_required(self):
        form = UserForm()
        self.assertTrue(form.fields['email'].required)

    def test_first_name_is_uneditable(self):
        form = UserForm()
        self.assertTrue(form.fields['first_name'].disabled)

    def test_last_name_is_uneditable(self):
        form = UserForm()
        self.assertTrue(form.fields['last_name'].disabled)

    def test_email_is_uneditable(self):
        form = UserForm()
        self.assertTrue(form.fields['email'].disabled)


class BookingFormTest(SimpleTestCase):
    def test_waiver_signed_field_label(self):
        form = BookingForm()
        self.assertTrue(form.fields['waiver_signed'].label == 'By signing up, I agree to Namaste Yoga Studio\'s liability waiver.')

    def test_waiver_signed_is_required(self):
        form = BookingForm()
        self.assertTrue(form.fields['waiver_signed'].required)

    def test_waiver_signed_is_a_checkbox(self):
        form = BookingForm()
        self.assertEqual(form.fields['waiver_signed'].widget.__class__.__name__, 'CheckboxInput')

