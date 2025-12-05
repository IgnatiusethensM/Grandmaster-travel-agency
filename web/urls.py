from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('safari-packages/', views.safari_packages, name='safari_packages'),
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('safari/<slug:slug>/', views.safari_package_detail, name='safari_package_detail'),
]
