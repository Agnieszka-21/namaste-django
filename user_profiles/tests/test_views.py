from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ..models import Profile


class HomeViewTest(SimpleTestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profiles/index.html')


class ProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up unmodified data for the entire TestCase
        """
        cls.test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        cls.profile = Profile.objects.get(
            user=cls.test_user
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        response = self.client.get(reverse(
            'profile', kwargs={'id': self.test_user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(
            reverse('profile', kwargs={'id': self.test_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profiles/profile.html')


class EditProfileViewTest(TestCase):

    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user.save()
        self.profile = Profile.objects.get(
            user=test_user
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser1')
        response = self.client.get(reverse(
            'edit_profile', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_user = User.objects.get(username='testuser1')
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(
            reverse('edit_profile', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profiles/profile_form.html')

    def test_redirects_to_my_bookings_upon_success(self):
        """
        Tests whether user is redirected to 'My account' (profile) page
        upon successful cancellation of their booking
        """
        test_user = User.objects.get(username='testuser1')
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        self.profile.injuries = 'carpal tunnel in the left wrist'
        self.profile.save()
        response = self.client.post(reverse(
            'edit_profile', kwargs={'id': test_user.id}),
            {'profile_updated': self.profile})
        self.assertRedirects(response, reverse(
            'profile', kwargs={'id': test_user.id}))
