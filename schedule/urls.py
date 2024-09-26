from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupClassList.as_view(), name='class_schedule'),
    path('book_class/<str:id>/', views.book_class, name='book_class'),
    path('book_class/<str:id>/dates/', views.create_dates, name='create_dates'),
    path('detail/<str:id>/', views.schedule_detail, name='schedule_detail'),
    path('my_bookings/<str:id>/', views.personal_bookings, name='my_bookings'),
    path('my_bookings/<str:id>/cancel_booking/<str:pk>/', views.cancel_booking, name='cancel_booking'),
    path('my_bookings/<str:id>/update_booking/<str:pk>/', views.update_booking, name='update_booking')
]