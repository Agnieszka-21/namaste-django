from django.urls import path
from .views import schedule, GroupClassList

urlpatterns = [
    path('', GroupClassList.as_view(), name='class_schedule'),
]