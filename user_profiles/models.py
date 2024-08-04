from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

# Helpful tutorials:
# https://dev.to/earthcomfy/django-user-profile-3hik
# https://forum.djangoproject.com/t/how-to-create-custom-users-with-different-roles-types/20772/5
# https://www.scaler.com/topics/django/profiles-and-groups-in-django/

class Client_User_Profile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)  # https://www.geeksforgeeks.org/uuidfield-django-models/
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_profile')
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    injuries = models.TextField(max_length=300, blank=True)
    profile_pic = CloudinaryField('image', default='placeholder')
    signed_waiver = models.BooleanField()

    def __str__(self):
        return str(self.first_name)

