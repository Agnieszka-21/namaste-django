from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

# Helpful tutorials:
# https://dev.to/earthcomfy/django-user-profile-3hik
# https://forum.djangoproject.com/t/how-to-create-custom-users-with-different-roles-types/20772/5
# https://www.scaler.com/topics/django/profiles-and-groups-in-django/

placeholder_image = '../static/images/default_profile_pic.jpg'

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)  # https://www.geeksforgeeks.org/uuidfield-django-models/
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    injuries = models.TextField(max_length=300, null=True, blank=True)
    profile_pic = CloudinaryField('image', default=placeholder_image, blank=True)
    signed_waiver = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()


