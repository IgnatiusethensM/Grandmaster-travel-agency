from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from packages.models import Package
from hotels.models import Hotel

@login_required
def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.total_price = package.price * booking.adults # Simplified logic
            booking.save()
            messages.success(request, 'Booking request submitted successfully!')
            return redirect('dashboard')
    else:
        initial_data = {
            'adults': request.GET.get('adults', 1),
            'check_in_date': request.GET.get('date'),
        }
        form = BookingForm(initial=initial_data)
    
    return render(request, 'bookings/form.html', {'form': form, 'package': package})

@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.hotel = hotel
            # Calculate days
            delta = booking.check_out_date - booking.check_in_date
            days = delta.days
            booking.total_price = hotel.price_per_night * days
            booking.save()
            messages.success(request, 'Hotel booking submitted successfully!')
            return redirect('dashboard')
    else:
        initial_data = {
            'check_in_date': request.GET.get('check_in'),
            'check_out_date': request.GET.get('check_out'),
        }
        form = BookingForm(initial=initial_data)
        
    return render(request, 'bookings/form.html', {'form': form, 'hotel': hotel})
