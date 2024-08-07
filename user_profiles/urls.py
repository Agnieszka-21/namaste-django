from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path('404/', views.error404, name='error404'),
]