from django.urls import path
from .views import profile, home, error404

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:pk>/', profile, name='profile'),
    path('404/', error404, name='error404'),
]