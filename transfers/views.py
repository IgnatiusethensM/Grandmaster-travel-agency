from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VehicleType, TransferBooking
from bookings.models import Booking
from decimal import Decimal
from datetime import datetime

def search_transfers(request):
    return render(request, 'transfers/search.html')

def transfer_results(request):
    pickup = request.GET.get('pickup')
    dropoff = request.GET.get('dropoff')
    date = request.GET.get('date')
    time = request.GET.get('time')
    passengers = int(request.GET.get('passengers', 1))
    
    # Mock distance calculation (random between 10 and 50 km)
    distance_km = Decimal(25.5) 
    
    vehicle_types = VehicleType.objects.all()
    
    # If no vehicle types exist, create some mock ones for display
    if not vehicle_types.exists():
        VehicleType.objects.create(name="Standard Sedan", capacity=3, base_rate=20, rate_per_km=1.5, image="https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=800&q=80", description="Comfortable ride for small groups")
        VehicleType.objects.create(name="Luxury SUV", capacity=5, base_rate=40, rate_per_km=2.5, image="https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800&q=80", description="Premium experience with extra space")
        VehicleType.objects.create(name="Executive Van", capacity=8, base_rate=60, rate_per_km=3.0, image="https://images.unsplash.com/photo-1565043666747-69f6646db940?auto=format&fit=crop&w=800&q=80", description="Ideal for larger groups and luggage")
        vehicle_types = VehicleType.objects.all()
        
    results = []
    for vt in vehicle_types:
        estimated_price = vt.base_rate + (vt.rate_per_km * distance_km)
        results.append({
            'vehicle': vt,
            'estimated_price': round(estimated_price, 2),
            'distance': distance_km
        })
        
    return render(request, 'transfers/results.html', {
        'results': results,
        'pickup': pickup,
        'dropoff': dropoff,
        'date': date,
        'time': time,
        'passengers': passengers
    })

@login_required
def book_transfer(request, vehicle_id):
    vehicle = get_object_or_404(VehicleType, id=vehicle_id)
    
    if request.method == 'POST':
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        price = Decimal(request.POST.get('price'))
        distance = Decimal(request.POST.get('distance'))
        
        # Combine date and time
        pickup_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        
        # Create Booking
        booking = Booking.objects.create(
            user=request.user,
            total_price=price,
            status='CONFIRMED',
            payment_status='PAID' # Mock payment
        )
        
        # Create TransferBooking
        TransferBooking.objects.create(
            booking=booking,
            vehicle_type=vehicle,
            pickup_location=pickup,
            dropoff_location=dropoff,
            pickup_time=pickup_time,
            distance_km=distance,
            driver_note=request.POST.get('notes', '')
        )
        
        return redirect('dashboard')
        
    context = {
        'vehicle': vehicle,
        'pickup': request.GET.get('pickup'),
        'dropoff': request.GET.get('dropoff'),
        'date': request.GET.get('date'),
        'time': request.GET.get('time'),
        'price': request.GET.get('price'),
        'distance': request.GET.get('distance')
    }
    return render(request, 'transfers/booking.html', context)
