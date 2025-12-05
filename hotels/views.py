from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .services import BookingService, HotelDTO
from bookings.models import Booking
from decimal import Decimal
import uuid

def hotel_list(request):
    # Redirect to search or results, or keep original logic
    # For now, let's redirect to search
    return redirect('search_hotels')

def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    return render(request, 'hotels/detail.html', {'hotel': hotel})

def search_hotels(request):
    return render(request, 'hotels/search.html')

def hotel_results(request):
    location = request.GET.get('location', '')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    guests = request.GET.get('guests', 1)
    
    # 1. Fetch Local Hotels
    local_hotels_qs = Hotel.objects.filter(location__icontains=location) if location else Hotel.objects.all()
    
    hotels = []
    for h in local_hotels_qs:
        hotels.append(HotelDTO(
            id=h.id,
            name=h.name,
            location=h.location,
            price=h.price_per_night,
            image=h.image.url if h.image else None,
            stars=h.stars,
            rating=h.rating,
            description=h.description,
            amenities=h.amenities,
            slug=h.slug,
            source='local'
        ))

    # 2. Fetch Booking.com Hotels (Mock)
    if location:
        service = BookingService()
        api_hotels = service.search_hotels(location, check_in, check_out, guests)
        hotels.extend(api_hotels)
        
    return render(request, 'hotels/results.html', {
        'hotels': hotels,
        'location': location,
        'check_in': check_in,
        'check_out': check_out,
        'guests': guests
    })

@login_required
def book_hotel(request, hotel_id):
    # Determine if it's a local or API hotel
    # Local IDs are integers, API IDs are strings (e.g., "bw_1")
    
    hotel = None
    is_api_hotel = False
    
    try:
        # Try to find local hotel first
        hotel = Hotel.objects.get(id=int(hotel_id))
    except (ValueError, Hotel.DoesNotExist):
        is_api_hotel = True
    
    if is_api_hotel:
        # It's an API hotel, we need to fetch details (mock) and create a local record if not exists
        # For simplicity in this mock, we'll recreate the hotel object from params or session if possible
        # But here we'll just create a dummy local record for the booking
        
        # Check if we already created a local record for this API hotel
        # In a real app, we'd map API ID to Local ID
        # For this demo, we'll create a new one based on POST data or just a placeholder
        
        if request.method == 'POST':
            hotel_name = request.POST.get('hotel_name')
            price = Decimal(request.POST.get('price'))
            
            # Create or get local hotel record
            hotel, created = Hotel.objects.get_or_create(
                name=hotel_name,
                defaults={
                    'location': 'External Location',
                    'price_per_night': price,
                    'description': 'Booked via External Partner',
                    'slug': f"ext-{uuid.uuid4()}"
                }
            )
    
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))
        total_price = Decimal(request.POST.get('total_price'))
        
        Booking.objects.create(
            user=request.user,
            hotel=hotel,
            check_in_date=check_in,
            check_out_date=check_out,
            adults=guests,
            total_price=total_price,
            status='CONFIRMED',
            payment_status='PAID' # Mock payment
        )
        return redirect('dashboard')

    # If GET, show booking form
    # We need to pass hotel details. If it's API, we might need to pass them via query params or session
    # For this implementation, we'll assume we pass basic info via GET params for API hotels
    
    context = {
        'hotel_id': hotel_id,
        'is_api': is_api_hotel,
        'check_in': request.GET.get('check_in'),
        'check_out': request.GET.get('check_out'),
        'guests': request.GET.get('guests'),
        'price': request.GET.get('price'),
        'name': request.GET.get('name')
    }
    
    if not is_api_hotel:
        context['hotel'] = hotel
        
    return render(request, 'hotels/booking.html', context)
