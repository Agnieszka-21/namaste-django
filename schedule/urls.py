from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupClassList.as_view(), name='class_schedule'),
    path('detail/<str:id>/', views.schedule_detail, name='schedule_detail')
]