from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('edit_profile/<str:id>/', views.editProfile, name='edit_profile')
]
