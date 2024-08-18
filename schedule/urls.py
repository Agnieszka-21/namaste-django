from django.urls import path
from .views import schedule, GroupClassList, schedule_detail

urlpatterns = [
    path('', GroupClassList.as_view(), name='class_schedule'),
    path('detail/', schedule_detail, name='schedule_detail')
]