from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import reverse
from ..models import YogaStyle, GroupClass, Booking
import uuid
from django.contrib.auth.models import User
from datetime import datetime
from datetime import timedelta


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
    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK', id=1)
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD', id=2)
        test_user1.save()
        test_user2.save()

        # Create a groupclass
        # test_groupclass = GroupClass.objects.create(weekday='Mon', start_time='1.05 pm')
        # test_genre = Genre.objects.create(name='Fantasy')
        # test_language = Language.objects.create(name='English')
        test_title = YogaStyle.objects.create(group_class_style='Express Lunchtime Yoga')
        test_groupclass = GroupClass.objects.create(
            title=test_title,
            weekday='Mon',
            start_time='1.05 pm',
        )

        # Create genre as a post-step
        # genre_objects_for_book = Genre.objects.all()
        # test_book.genre.set(genre_objects_for_book) # Direct assignment of many-to-many types not allowed.
        # test_book.save()

        # Create a BookingInstance object for test_user1
        # return_date = datetime.date.today() + datetime.timedelta(days=5)
        self.test_booking1 = Booking.objects.create(
            id=12345,
            chosen_class=test_groupclass,
            client=test_user2,
            class_datetime=datetime.now() + timedelta(days=10),
            booking_time=datetime.now() - timedelta(days=3),
            waiver_signed=True,
            booking_cancelled=False,
            cancellation_reason=None
        )

        # Create a BookInstance object for test_user2
        # return_date = datetime.date.today() + datetime.timedelta(days=5)
        # self.test_bookinstance2 = BookInstance.objects.create(
        #     book=test_book,
        #     imprint='Unlikely Imprint, 2016',
        #     due_back=return_date,
        #     borrower=test_user2,
        #     status='o',
        # )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('cancel_booking'), kwargs={'id': self.test_user2.id, 'pk': self.test_booking1.id})
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    # def test_uses_correct_template(self):
    #     login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
    #     response = self.client.get(reverse('cancel_booking', kwargs={'[pk]': self.test_booking1.pk}))
    #     self.assertEqual(response.status_code, 200)
    #     # Check we used correct template
    #     self.assertTemplateUsed(response, 'schedule/cancel_booking.html')