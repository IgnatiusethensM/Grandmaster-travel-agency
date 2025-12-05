from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import FlightSearchService
from .models import Flight, FlightBooking
from bookings.models import Booking

def search_flights(request):
    if request.method == 'GET':
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        date = request.GET.get('date')
        
        if origin and destination and date:
            service = FlightSearchService()
            flights = service.search(origin, destination, date)
            return render(request, 'flights/results.html', {
                'flights': flights,
                'origin': origin,
                'destination': destination,
                'date': date
            })
            
    return render(request, 'flights/search.html')

@login_required
def book_flight(request, flight_id):
    # In a real app, we would fetch the flight from the database or the API
    # For this mock, we'll reconstruct the flight object or use a mock one
    # For simplicity, let's assume we pass flight details via session or re-fetch
    
    if request.method == 'POST':
        # Create Booking
        booking = Booking.objects.create(
            user=request.user,
            booking_type='FLIGHT',
            status='CONFIRMED',
            total_price=request.POST.get('price')
        )
        
        # Create FlightBooking
        # Note: In a real scenario, we'd need to save the Flight object first if it doesn't exist
        # For this mock, we'll skip saving the Flight object to DB to avoid complexity with mock data
        # and just save the booking reference. 
        # Ideally, we should have a 'Flight' record for every bookable flight.
        
        return redirect('dashboard')
        
    return render(request, 'flights/booking.html', {'flight_id': flight_id})
