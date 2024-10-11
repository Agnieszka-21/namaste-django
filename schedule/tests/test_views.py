from datetime import date, datetime, timedelta
from dateutil import parser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils.timezone import make_aware
import uuid
from ..models import YogaStyle, GroupClass, Booking, SpecificGroupClass
from django.contrib.messages import get_messages


class ScheduleViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('/schedule/')
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
    @classmethod
    def setUpTestData(cls):
        """
        Creates a user to test the url
        """
        cls.user = User.objects.create(username='testuser1')

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(
            reverse('my_bookings', kwargs={'id': self.user.id}))
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


class PersonalBookingsViewTest(TestCase):

    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user.save()

        test_user2 = User.objects.create_user(
            username='testuser2', password='2X<ISRUkw+tuK', id=2)
        test_user2.save()

        test_booking1 = Booking.objects.create(
            client=test_user,
            class_datetime=make_aware(parser.parse('2025-12-27 08:30:00'))
            )
        test_booking2 = Booking.objects.create(
            client=test_user,
            class_datetime=make_aware(parser.parse('2025-12-20 08:30:00'))
            )
        test_booking3 = Booking.objects.create(
            client=test_user2,
            class_datetime=make_aware(parser.parse('2025-11-20 08:30:00'))
            )

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser1')
        response = self.client.get(reverse(
            'my_bookings', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_user = User.objects.get(username='testuser1')
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(
            reverse('my_bookings', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        test_user = User.objects.get(username='testuser1')
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(
            reverse('my_bookings', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/personal_bookings.html')

    def test_view_filters_bookings_by_client(self):
        """
        Tests whether the view shows only the bookings made
        by the specific logged-in user
        """
        test_user = User.objects.get(username='testuser1')
        test_booking1 = Booking.objects.get(
            class_datetime=make_aware(parser.parse('2025-12-27 08:30:00'))
            )
        test_booking2 = Booking.objects.get(
            class_datetime=make_aware(parser.parse('2025-12-20 08:30:00'))
            )
        test_booking3 = Booking.objects.get(
            class_datetime=make_aware(parser.parse('2025-11-20 08:30:00'))
            )
        personal_bookings = Booking.objects.filter(client=test_user)
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(reverse(
            'my_bookings', kwargs={'id': test_user.id}))
        self.assertEqual(len(personal_bookings), 2)
        # Check the ordering of bookings by class_datetime
        self.assertEqual(personal_bookings[0], test_booking2)
        self.assertEqual(personal_bookings[1], test_booking1)


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


class RemoveParticipantViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user1.save()
        test_user2 = User.objects.create_user(
            username='testuser2', password='2X<ISRUkw+tuK', id=2)
        test_user2.save()
        orig_spec_class = SpecificGroupClass.objects.create(
            id='97668496-7f8c-44b3-887d-e856c6029bf9',
            num_of_participants=2)
        orig_spec_class.participants_names.set([test_user1, test_user2])
        chosen_booking = Booking.objects.create(
            id='c0f55889-daa4-473f-b402-8495000757ff',
            client=test_user1)

    def test_view_removes_participant(self):
        """
        Tests whether the number of participants is decreased
        and the name of the client who cancelled their booking
        has been removed from the list of participants
        """
        orig_spec_class = SpecificGroupClass.objects.get(
            id='97668496-7f8c-44b3-887d-e856c6029bf9')
        chosen_booking = Booking.objects.get(
            id='c0f55889-daa4-473f-b402-8495000757ff')
        test_user1 = User.objects.get(username='testuser1')
        test_user2 = User.objects.get(username='testuser2')
        orig_spec_class.num_of_participants -= 1
        orig_spec_class.participants_names.remove(chosen_booking.client)
        self.assertEqual(orig_spec_class.num_of_participants, 1)
        self.assertTrue(test_user2 in orig_spec_class.participants_names.all())
        self.assertFalse(
            test_user1 in orig_spec_class.participants_names.all())


class BookClassViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified
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
            'book_class', kwargs={'id': test_user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))


class UpdateBookingViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified
        """
        test_user = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user.save()
        test_booking = Booking.objects.create(
            id='97668496-7f8c-44b3-887d-e856c6029bf9')

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser1')
        test_booking = Booking.objects.get(
            id='97668496-7f8c-44b3-887d-e856c6029bf9')
        response = self.client.get(reverse(
            'update_booking', kwargs={
                'id': test_user.id, 'pk': test_booking.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))
