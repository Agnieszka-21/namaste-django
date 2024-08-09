from django.apps import AppConfig


class UserProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profiles'

    #def ready(self):
        # Import your signal file in here if the app is ready. From https://stackoverflow.com/questions/63057047/how-to-automatically-create-user-profile-for-new-users-that-register-to-the-plat
        #from . import receivers
