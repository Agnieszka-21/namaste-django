from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import YogaStyle, GroupClass, Booking
import uuid
from django.contrib.auth.models import User
from datetime import datetime
from datetime import timedelta
from django.utils.timezone import make_aware


class GroupClassListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 12 groupclasses
        number_of_groupclasses = 12

        for id in range(number_of_groupclasses):
            GroupClass.objects.create(
                weekday = f'Mon {id}',
                start_time=f'1.05 pm {id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/schedule/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('class_schedule'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('class_schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/schedule_list.html')

    def test_lists_all_groupclasses(self):
        # Confirm the list has (exactly) 12 items, all on one page
        response = self.client.get(reverse('class_schedule')+'?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertFalse(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['groupclass_list']), 12)


class ScheduleDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a few groupclasses
        number_of_groupclasses = 12

        for id in range(number_of_groupclasses):
            cls.groupclass = GroupClass.objects.create(
                weekday = f'Mon {id}',
                start_time=f'1.05 pm {id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/schedule/detail/12/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/schedule/detail/13/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('schedule_detail', kwargs={'id': self.groupclass.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('schedule_detail', kwargs={'id': self.groupclass.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/schedule_detail.html')


class CancelBookingViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK', id=1)
        cls.test_yogastyle = YogaStyle.objects.create(group_class_style='Express Lunchtime Yoga')
        cls.test_groupclass = GroupClass.objects.create(title=cls.test_yogastyle)
        cls.test_booking = Booking.objects.create(
            id=uuid.uuid4(),
            chosen_class=cls.test_groupclass,
            client=cls.test_user,
            class_datetime=make_aware(datetime.now() + timedelta(days=10)),
            booking_time=make_aware(datetime.now() - timedelta(days=3)),
            waiver_signed=True,
            booking_cancelled=False,
            cancellation_reason=None
        )

    def test_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('cancel_booking', kwargs={'id': self.test_user.id, 'pk': self.test_booking.id}))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable) ??? check if this is true
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_uses_correct_template(self):
        logged_in = self.client.login(username='testuser1', password='1X<ISRUkw+tuK', id=1)
        response = self.client.get(reverse('cancel_booking', kwargs={'id': self.test_user.id, 'pk': self.test_booking.id}))
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'schedule/cancel_booking.html')
