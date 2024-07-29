from django.urls import path
from .views import profile, home

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
]