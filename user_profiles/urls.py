from django.urls import path
from .views import profile, home, error404, editProfile

urlpatterns = [
    path('', home, name='home'),
    #path('profile/', profile, name='profile'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', editProfile, name='edit_profile'),
    path('404/', error404, name='error404'),
]