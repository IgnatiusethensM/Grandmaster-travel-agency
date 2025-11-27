from django.shortcuts import render, get_object_or_404
from .models import Hotel
from .services import BookingService, HotelDTO

def hotel_list(request):
    # 1. Fetch Local Hotels
    local_hotels_qs = Hotel.objects.all()
    
    location_filter = request.GET.get('location', '')
    stars_filter = request.GET.get('stars')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    
    if location_filter:
        local_hotels_qs = local_hotels_qs.filter(location__icontains=location_filter)
    if stars_filter:
        local_hotels_qs = local_hotels_qs.filter(stars=stars_filter)
    
    # Convert local hotels to DTOs
    hotels = []
    for h in local_hotels_qs:
        hotels.append(HotelDTO(
            id=h.id,
            name=h.name,
            location=h.location,
            price=h.price_per_night,
            image=h.image.url if h.image else None,
            stars=h.stars,
            rating=8.5, # Placeholder for local rating
            description=h.description,
            amenities=h.amenities,
            slug=h.slug,
            source='local'
        ))

    # 2. Fetch Booking.com Hotels (only if searching)
    if location_filter:
        service = BookingService()
        api_hotels = service.search_hotels(location_filter, check_in, check_out)
        hotels.extend(api_hotels)
        
    return render(request, 'hotels/list.html', {'hotels': hotels})

def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    return render(request, 'hotels/detail.html', {'hotel': hotel})
