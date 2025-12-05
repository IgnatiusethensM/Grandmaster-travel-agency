from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('safari-packages/', views.safari_packages, name='safari_packages'),
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
]
