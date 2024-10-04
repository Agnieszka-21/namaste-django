from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile
# import uuid


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create_user(id=12345, username='minnie', password='MiNi4eveR', first_name='Minnie', last_name='Mouse')
        cls.profile = cls.user.profile

    def test_injuries_max_length(self):
        profile = Profile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('injuries').max_length
        self.assertEqual(max_length, 300)

    def test_str_representation_is_first_and_last_name(self):
        test_profile = Profile.objects.get(id=self.profile.id)
        expected_str = f'{test_profile.user.first_name} {test_profile.user.last_name}'
        self.assertEqual(str(test_profile), expected_str)
