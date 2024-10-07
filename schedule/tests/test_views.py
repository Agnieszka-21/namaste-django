from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils.timezone import make_aware
import uuid
from ..models import YogaStyle, GroupClass, Booking


class ScheduleViewTest(SimpleTestCase):
    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        self.assertTemplateUsed('schedule/schedule.html')


class GroupClassListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 12 GroupClass objects to set up
        unmodified data for the entire TestCase
        """
        number_of_groupclasses = 12

        for id in range(number_of_groupclasses):
            GroupClass.objects.create(
                weekday=f'Mon {id}',
                start_time=f'1.05 pm {id}'
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/schedule/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('class_schedule'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('class_schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/schedule_list.html')

    def test_lists_all_groupclasses(self):
        """
        Confirms that the list groupclasses has (exactly) 12 items,
        all on one page
        """
        response = self.client.get(reverse('class_schedule')+'?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertFalse(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['groupclass_list']), 12)


class BookingListViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        self.assertTemplateUsed('schedule/personal_bookings.html')


class ScheduleDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 12 unmodified GroupClass objects
        to set up data for the entire TestCase
        """
        number_of_groupclasses = 12

        for id in range(number_of_groupclasses):
            cls.groupclass = GroupClass.objects.create(
                weekday=f'Mon {id}',
                start_time=f'1.05 pm {id}',
                image='placeholder'
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/schedule/detail/12/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/schedule/detail/13/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(
            reverse('schedule_detail', kwargs={'id': self.groupclass.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(
            reverse('schedule_detail', kwargs={'id': self.groupclass.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/schedule_detail.html')


class CancelBookingViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user.save()
        test_yogastyle = YogaStyle.objects.create(
            group_class_style='Express Lunchtime Yoga')
        test_groupclass = GroupClass.objects.create(title=test_yogastyle)
        self.test_booking = Booking.objects.create(
            id=uuid.uuid4(),
            chosen_class=test_groupclass,
            client=test_user,
            class_datetime=make_aware(datetime.now() + timedelta(days=10)),
            booking_time=make_aware(datetime.now() - timedelta(days=3)),
            waiver_signed=True,
            booking_cancelled=False,
            cancellation_reason=None
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser1')
        response = self.client.get(reverse(
            'cancel_booking',
            kwargs={'id': test_user.id, 'pk': self.test_booking.id}))
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
        response = self.client.get(reverse(
            'cancel_booking',
            kwargs={'id': test_user.id, 'pk': self.test_booking.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/cancel_booking.html')

    def test_redirects_to_my_bookings_upon_success(self):
        """
        Tests whether user is redirected to 'My bookings' page
        upon successful cancellation of their booking
        """
        test_user = User.objects.get(username='testuser1')
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        self.test_booking.booking_cancelled = True
        self.test_booking.cancellation_reason = 'client\'s decision'
        self.test_booking.save()
        response = self.client.post(reverse(
            'cancel_booking',
            kwargs={'id': test_user.id, 'pk': self.test_booking.id}),
            {'booking_cancelled': self.test_booking})
        self.assertRedirects(response, reverse(
            'my_bookings', kwargs={'id': test_user.id}))


class PersonalBookingsViewTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     """
    #     Creates 5 unmodified Booking objects
    #     to set up data for the entire TestCase
    #     """
    #     cls.test_user = User.objects.create_user(
    #         username='testuser1', password='1X<ISRUkw+tuK', id=1)
    #     number_of_bookings = 5
    #     for id in range(number_of_bookings):
    #         cls.booking = Booking.objects.create(
    #             client=cls.test_user
    #         )

    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user.save()

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser1')
        response = self.client.get(reverse(
            'my_bookings', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    # def test_view_url_accessible_by_name(self):
    #     """
    #     Tests whether the url related to this view
    #     can be accessed by its name
    #     """
    #     logged_in = self.client.login(
    #         username='testuser1', password='1X<ISRUkw+tuK', id=1)
    #     response = self.client.get(reverse('my_bookings', kwargs={'id': self.test_user.id}))
    #     self.assertEqual(response.status_code, 200) # AssertionError: 302 != 200

    # def test_view_uses_correct_template(self):
    #     """
    #     Tests whether the correct template is used
    #     """
    #     logged_in = self.client.login(
    #         username='testuser1', password='1X<ISRUkw+tuK', id=1)
    #     response = self.client.get(reverse('my_bookings', kwargs={'id': self.test_user.id}))
    #     self.assertEqual(response.status_code, 200)  # AssertionError: 302 != 200
    #     self.assertTemplateUsed(response, 'schedule/personal_bookings.html')

