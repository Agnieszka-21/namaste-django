from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import make_aware
from ..models import YogaStyle, StyleDescription, GroupClass
from ..models import Booking, SpecificGroupClass
from pytz import timezone


class YogaStyleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified YogaStyle object
        used by all test methods
        """
        YogaStyle.objects.create(group_class_style='Express Lunchtime Yoga')

    def test_group_class_style_label(self):
        """
        Tests the verbose name of the field 'group_class_style'
        """
        style = YogaStyle.objects.get(id=1)
        field_label = style._meta.get_field('group_class_style').verbose_name
        self.assertEqual(field_label, 'group class style')

    def test_group_class_style_max_length(self):
        """
        Tests the maximum length of the field 'group_class_style'
        """
        style = YogaStyle.objects.get(id=1)
        max_length = style._meta.get_field('group_class_style').max_length
        self.assertEqual(max_length, 30)

    def test_str_representation_is_group_class_style(self):
        """
        Tests the string representation of the field 'group_class_style'
        """
        style = YogaStyle.objects.get(id=1)
        expected_str = f'{style.group_class_style}'
        self.assertEqual(str(style), expected_str)


class StyleDescriptionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified StyleDescription object
        used by all test methods
        """
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
        """
        Tests the verbose name of the field 'group_class_description'
        """
        description = StyleDescription.objects.get(id=1)
        field_label = description._meta.get_field(
            'group_class_description').verbose_name
        self.assertEqual(field_label, 'group class description')

    def test_group_class_description_max_length(self):
        """
        Tests the maximum length of the field 'group_class_description'
        """
        description = StyleDescription.objects.get(id=1)
        max_length = description._meta.get_field(
            'group_class_description').max_length
        self.assertEqual(max_length, 5000)

    def test_str_representation_is_group_class_description(self):
        """
        Tests the string representation of the field 'group_class_description'
        """
        description = StyleDescription.objects.get(id=1)
        expected_str = f'{description.group_class_description}'
        self.assertEqual(str(description), expected_str)


class GroupClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified GroupClass object as well as its Foreign Keys
        (YogaStyle object and StyleDescription object) used by all test methods
        """
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
        cls.description = StyleDescription.objects.create(
            group_class_description=cls.description_)
        cls.groupclass = GroupClass.objects.create(
            title=cls.title,
            description=cls.description,
            weekday='Mon',
            start_time='1.05 pm',
            duration_mins=60,
            location='Studio 1',
            teacher='Mary Dawson',
            teacher_bio=(
                "Mary is +500-hour qualified yoga teacher. She teaches yoga "
                "with an emphasis on safety and alignment. This offers "
                "students a supportive environment to explore their personal "
                "yoga practice. Mary began practising yoga in 2012. Her "
                "interest derived from the desire to balance out a busy "
                "lifestyle. Finding a new level of stillness, she is now on "
                "a mission to share the benefits  of yoga with everyone! "
                "She will continue her mission by going to training and "
                "events to improve her teaching skills."
                )
        )

    def test_if_groupclass_has_a_title(self):
        """
        Tests whether a GroupClass object has a title
        (Foreign Key)
        """
        self.assertEqual(self.groupclass.title.group_class_style, self.title_)

    def test_if_groupclass_has_a_description(self):
        """
        Tests whether a GroupClass object has a description
        (Foreign Key)
        """
        self.assertEqual(
            self.groupclass.description.group_class_description,
            self.description_)

    def test_groupclass_weekday_max_length(self):
        """
        Tests the maximum length of the field 'weekday'
        """
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('weekday').max_length
        self.assertEqual(max_length, 10)

    def test_groupclass_start_time_max_length(self):
        """
        Tests the maximum length of the field 'start_time'
        """
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('start_time').max_length
        self.assertEqual(max_length, 10)

    def test_groupclass_location_max_length(self):
        """
        Tests the maximum length of the field 'location'
        """
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('location').max_length
        self.assertEqual(max_length, 20)

    def test_groupclass_teacher_max_length(self):
        """
        Tests the maximum length of the field 'teacher'
        """
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('teacher').max_length
        self.assertEqual(max_length, 100)

    def test_groupclass_teacher_bio_max_length(self):
        """
        Tests the maximum length of the field 'teacher_bio'
        """
        groupclass = GroupClass.objects.get(id=1)
        max_length = groupclass._meta.get_field('teacher_bio').max_length
        self.assertEqual(max_length, 3000)

    def test_groupclass_verbose_name_plural(self):
        """
        Tests the plural verbose name of the GroupClass object that was
        set explicitly since the default version was grammatically
        incorrect
        """
        groupclass = GroupClass.objects.get(id=1)
        verbose_name_plural = groupclass._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'group classes')

    def test_str_representation_of_groupclass(self):
        """
        Tests the string representation of the GroupClass object
        """
        groupclass = GroupClass.objects.get(id=1)
        expected_str = (
            f'{groupclass.title} | {groupclass.weekday} '
            f'{groupclass.start_time}')
        self.assertEqual(str(groupclass), expected_str)


class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Booking object as well as its Foreign Keys
        (both direct and indirect) used by all test methods
        """
        cls.chosen_class_title_ = 'Express Lunchtime Yoga'
        cls.title = YogaStyle.objects.create(
            group_class_style=cls.chosen_class_title_)
        cls.chosen_class_weekday = 'Mon'
        cls.chosen_class_start_time = '1.05 pm'
        cls.chosen_class = (
            cls.chosen_class_title_ + '  | ' + cls.chosen_class_weekday +
            ' ' + cls.chosen_class_start_time)
        cls.chosen_class = GroupClass.objects.create(
            title=cls.title,
            weekday=cls.chosen_class_weekday,
            start_time=cls.chosen_class_start_time)
        cls.client_ = 'Jane Doe'
        cls.client = User.objects.create(username=cls.client_)
        cls.current_datetime_ = datetime.now()
        cls.current_datetime = make_aware(cls.current_datetime_)
        cls.booking = Booking.objects.create(
            id=1,
            chosen_class=cls.chosen_class,
            client=cls.client,
            booking_time=cls.current_datetime,
            waiver_signed=True
        )

    def test_if_booking_has_a_chosen_class(self):
        """
        Tests whether the Booking object has a chosen_class
        (Foreign Key)
        """
        self.assertEqual(
            str(self.booking.chosen_class.title), self.chosen_class_title_)

    def test_if_booking_has_a_client(self):
        """
        Tests whether the Booking object has a client
        (Foreign Key)
        """
        self.assertEqual(str(self.booking.client), self.client_)

    def test_if_booking_waiver_signed_is_true(self):
        """
        Tests whether the field 'waiver_signed' is True
        """
        self.assertTrue(self.booking.waiver_signed)

    def test_if_booking_cancelled_is_false(self):
        """
        Tests whether the value of the field 'booking_cancelled'
        is False by default
        """
        self.assertFalse(self.booking.booking_cancelled)

    def test_if_booking_time_is_now(self):
        """
        Tests whether the field value of 'booking_time' is equal to
        current time (without milliseconds)
        """
        # https://blog.finxter.com/5-best-ways-to-remove-milliseconds-from-python-datetime/
        datetime_now = datetime.now()
        formatted_datetime_now = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(
            self.booking.booking_time.strftime(
                '%Y-%m-%d %H:%M:%S'), formatted_datetime_now)

    def test_str_representation_of_booking(self):
        """
        Tests the string representation of the Booking object
        """
        booking = Booking.objects.get(id=1)
        expected_str = (
            f"{booking.booking_time} | Booking {booking.id} | Client: "
            f"{booking.client} | {booking.chosen_class.title} | On "
            f"{booking.class_datetime} | Cancelled: "
            f"{booking.booking_cancelled}")
        self.assertEqual(str(booking), expected_str)


class SpecificGroupClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified SpecificGroupClass object used by all test methods
        """
        cls.specific_groupclass = SpecificGroupClass.objects.create(
            id=1,
            specific_title='Express Lunchtime Yoga',
            specific_datetime=make_aware(datetime.now()),
            num_of_participants=2,
        )
        # cls.specific_groupclass.participants_names.set(
        # ['Jane Doe', 'John Doe'])

    def test_specific_groupclass_verbose_name_plural(self):
        """
        Tests the plural verbose name of the SpecificGroupClass object
        that was set explicitly since the default version was grammatically
        incorrect
        """
        specific_groupclass = SpecificGroupClass.objects.get(id=1)
        verbose_name_plural = specific_groupclass._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'specific group classes')

    def test_str_representation_of_specific_groupclass(self):
        """
        Tests the string representation of the SpecificGroupClass object
        """
        specific_gc = SpecificGroupClass.objects.get(id=1)
        expected_str = (f"{specific_gc.specific_title} | "
                        "{specific_gc.specific_datetime} | {specific_gc.id}")
        self.assertEqual(str(specific_gc), expected_str)
