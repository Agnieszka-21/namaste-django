from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupClassList.as_view(), name='class_schedule'),
    path('detail/<str:id>/', views.schedule_detail, name='schedule_detail'),
    path('book_class/<str:id>/', views.book_class, name='book_class'),
    #path('book_class/<int:pk>/', views.Booking.as_view(), name='book_class'),
]