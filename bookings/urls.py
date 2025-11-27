from django.urls import path
from . import views

urlpatterns = [
    path('package/<int:package_id>/', views.book_package, name='book_package'),
    path('hotel/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
]
