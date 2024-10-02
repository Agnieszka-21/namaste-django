from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import YogaStyle, StyleDescription, GroupClass, Booking, SpecificGroupClass


class YogaStyleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        YogaStyle.objects.create(group_class_style='Express Lunchtime Yoga')

    def test_group_class_style_label(self):
        style = YogaStyle.objects.get(id=1)
        field_label = style._meta.get_field('group_class_style').verbose_name
        self.assertEqual(field_label, 'group class style')

    def test_group_class_style_max_length(self):
        style = YogaStyle.objects.get(id=1)
        max_length = style._meta.get_field('group_class_style').max_length
        self.assertEqual(max_length, 30)

    def test_str_representation_is_group_class_style(self):
        style = YogaStyle.objects.get(id=1)
        expected_str = f'{style.group_class_style}'
        self.assertEqual(str(style), expected_str)


class StyleDescriptionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        StyleDescription.objects.create(group_class_description=(
        "The beginners' yoga class is a great way to start your "
        "yoga journey. Students will learn yogic breathing, yoga "
        "postures, and relaxation techniques. It is the perfect class to "
        "build a strong foundation for yourself. The beginners yoga class "
        "is there to help you feel safe and supported in your practice. "
        "This class will help you build strength and mobility as well as "
        "cultivate a calmer mind. "
        "Not suitable for prenatal students."
        ))

    def test_group_class_description_label(self):
        description = StyleDescription.objects.get(id=1)
        field_label = description._meta.get_field('group_class_description').verbose_name
        self.assertEqual(field_label, 'group class description')

    def test_group_class_description_max_length(self):
        description = StyleDescription.objects.get(id=1)
        max_length = description._meta.get_field('group_class_description').max_length
        self.assertEqual(max_length, 5000)

    def test_str_representation_is_group_class_description(self):
        description = StyleDescription.objects.get(id=1)
        expected_str = f'{description.group_class_description}'
        self.assertEqual(str(description), expected_str)


class GroupClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.title_ = 'Express Lunchtime Yoga'
        cls.title = YogaStyle.objects.create(group_class_style=cls.title_)
        cls.description_ = (
            "The beginners' yoga class is a great way to start your "
            "yoga journey. Students will learn yogic breathing, yoga "
            "postures, and relaxation techniques. It is the perfect class to "
            "build a strong foundation for yourself. The beginners yoga class "
            "is there to help you feel safe and supported in your practice. "
            "This class will help you build strength and mobility as well as "
            "cultivate a calmer mind. "
            "Not suitable for prenatal students."
            )
        cls.description = StyleDescription.objects.create(group_class_description=cls.description_)
        cls.groupclass = GroupClass.objects.create(
            title=cls.title,
            description=cls.description,
            weekday='Mon',
            start_time='1.05 pm',
            duration_mins=60,
            location='Studio 1',
            teacher='Mary Dawson',
            teacher_bio=(
                "Mary is +500-hour qualified yoga teacher. She teaches yoga with an "
                "emphasis on safety and alignment. This offers students a supportive "
                "environment to explore their personal yoga practice. Mary began practising "
                "yoga in 2012. Her interest derived from the desire to balance out a busy lifestyle. "
                "Finding a new level of stillness, she is now on a mission to share the benefits "
                "of yoga with everyone! She will continue her mission by going to training and events "
                "to improve her teaching skills."
                )
        )

    def test_if_groupclass_has_a_title(self):
        self.assertEqual(self.groupclass.title.group_class_style, self.title_)

    def test_if_groupclass_has_a_description(self):
        self.assertEqual(self.groupclass.description.group_class_description, self.description_)

    def test_groupclass_weekday_max_length(self):
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('weekday').max_length
        self.assertEqual(max_length, 10)

    def test_groupclass_start_time_max_length(self):
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('start_time').max_length
        self.assertEqual(max_length, 10)

    def test_groupclass_location_max_length(self):
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('location').max_length
        self.assertEqual(max_length, 20)

    def test_groupclass_teacher_max_length(self):
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('teacher').max_length
        self.assertEqual(max_length, 100)

    def test_groupclass_teacher_bio_max_length(self):
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('teacher_bio').max_length
        self.assertEqual(max_length, 3000)

    def test_groupclass_verbose_name_plural(self):
        groupclass = GroupClass.objects.get(id=1)        
        verbose_name_plural = groupclass._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'group classes')

    # def test_groupclass_ordering(self):
    #     groupclass = GroupClass.objects.get(id=1)        
    #     ordering = groupclass._meta.ordering
    #     self.assertEqual(ordering, ['first_class__week_day', 'start_time'])

    def test_str_representation_of_groupclass(self):
        groupclass = GroupClass.objects.get(id=1)
        expected_str = f'{groupclass.title} | {groupclass.weekday} {groupclass.start_time}'
        self.assertEqual(str(groupclass), expected_str)


class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.chosen_class_ = 'Express Lunchtime Yoga'
        cls.title = YogaStyle.objects.create(group_class_style=cls.chosen_class_)
        cls.chosen_class = GroupClass.objects.create(title=cls.title)
        cls.client_ = 'Jane Doe'
        cls.client = User.objects.create(username=cls.client_)
        cls.booking = Booking.objects.create(
            id=1,
            chosen_class=cls.chosen_class,
            client=cls.client,
            # booking_time=timezone.now(),
            waiver_signed=True
        )

    def test_if_booking_has_a_chosen_class(self):
        self.assertEqual(str(self.booking.chosen_class.title), self.chosen_class_)

    def test_if_booking_has_a_client(self):
        self.assertEqual(str(self.booking.client), self.client_)

    def test_if_booking_waiver_signed_is_true(self):
        self.assertTrue(self.booking.waiver_signed)

    def test_if_booking_cancelled_is_false(self):
        self.assertFalse(self.booking.booking_cancelled)

    def test_if_booking_time_is_now(self):
        # https://blog.finxter.com/5-best-ways-to-remove-milliseconds-from-python-datetime/
        datetime_now = timezone.now()
        formatted_datetime_now = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(self.booking.booking_time.strftime('%Y-%m-%d %H:%M:%S'), formatted_datetime_now)
