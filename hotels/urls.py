from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('<slug:slug>/', views.hotel_detail, name='hotel_detail'),
    path('<int:hotel_id>/book/', views.hotel_detail, name='book_hotel'), # Placeholder for booking
]
