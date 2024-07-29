from django.db import models
from django.contrib.auth.models import User
# import uuid

# Helpful tutorials:
# https://dev.to/earthcomfy/django-user-profile-3hik
# https://forum.djangoproject.com/t/how-to-create-custom-users-with-different-roles-types/20772/5
# https://www.scaler.com/topics/django/profiles-and-groups-in-django/

class Client_User_Profile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # https://www.geeksforgeeks.org/uuidfield-django-models/
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    injuries = models.TextField(max_length=300, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    # profile_pic = CloudinaryField()
    signed_waiver = models.BooleanField()

