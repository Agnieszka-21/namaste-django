from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Profile(models.Model):
    """
    Django database profile model for maintaining
    additional information about each user who creates
    an account
    """
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    injuries = models.TextField(max_length=300, null=True, blank=True)
    profile_pic = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)


# The following function been copied from CI's walkthrough project Boutique Ado
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create a new profile when a user is created
    or save changes to the existing profile
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
