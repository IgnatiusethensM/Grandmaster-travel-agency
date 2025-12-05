from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_hotels, name='search_hotels'),
    path('results/', views.hotel_results, name='hotel_results'),
    path('book/<str:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('', views.hotel_list, name='hotel_list'),
    path('<slug:slug>/', views.hotel_detail, name='hotel_detail'),
]
