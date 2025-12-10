from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/booking/<int:booking_id>/update/', views.update_booking_status, name='update_booking_status'),
]
