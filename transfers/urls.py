from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_transfers, name='search_transfers'),
    path('results/', views.transfer_results, name='transfer_results'),
    path('book/<int:vehicle_id>/', views.book_transfer, name='book_transfer'),
]
