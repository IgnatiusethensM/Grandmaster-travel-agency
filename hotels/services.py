import requests
import random
from decimal import Decimal
from datetime import timedelta
from django.conf import settings

class HotelDTO:
    """
    Data Transfer Object to unify local and API hotel data.
    """
    def __init__(self, id, name, location, price, image, stars, rating, description, amenities, slug=None, source='local'):
        self.id = id
        self.name = name
        self.slug = slug
        self.location = location
        self.price = price
        self.image = image
        self.stars = stars
        self.rating = rating
        self.description = description
        self.amenities = amenities
        self.source = source # 'local' or 'booking_com'

class BookingService:
    """
    Service to interact with Booking.com API (Demand API).
    """
    BASE_URL = "https://distribution-xml.booking.com/2.0/json" # Example endpoint

    def __init__(self):
        self.api_key = getattr(settings, 'BOOKING_COM_API_KEY', None)
        self.affiliate_id = getattr(settings, 'BOOKING_COM_AFFILIATE_ID', None)

    def search_hotels(self, location, check_in, check_out, guests=1):
        if not self.api_key:
            return MockBookingService().search_hotels(location, check_in, check_out, guests)
        
        # Real API implementation would go here
        # params = {
        #     'city_name': location,
        #     'checkin': check_in,
        #     'checkout': check_out,
        #     'guests': guests
        # }
        # response = requests.get(f"{self.BASE_URL}/hotelAvailability", params=params, auth=(self.api_key, ''))
        # return self._parse_response(response.json())
        return []

class MockBookingService:
    """
    Mock service to simulate Booking.com API responses.
    """
    def search_hotels(self, location, check_in, check_out, guests=1):
        # Return some dummy data that looks like Booking.com results
        # In a real scenario, we would filter by location, but for mock we just return random results if location matches loosely
        
        mock_images = [
            "https://cf.bstatic.com/xdata/images/hotel/max1024x768/467786274.jpg?k=5347209760773067607730676077306760773067607730676077306760773067&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max1024x768/498305385.jpg?k=5347209760773067607730676077306760773067607730676077306760773067&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max1024x768/12345678.jpg?k=5347209760773067607730676077306760773067607730676077306760773067&o=&hp=1",
        ]

        results = []
        # Generate 5 mock hotels
        for i in range(1, 6):
            price = Decimal(random.randint(5000, 50000))
            results.append(HotelDTO(
                id=f"bw_{i}", # booking_com_id
                name=f"Booking.com Hotel {i} - {location.title() if location else 'City Center'}",
                location=location.title() if location else "Nairobi",
                price=price,
                image=random.choice(mock_images),
                stars=random.randint(3, 5),
                rating=round(random.uniform(7.0, 9.8), 1),
                description="Experience world-class service at this property. Located in the heart of the city, offering luxury amenities and comfortable stays.",
                amenities=["Free WiFi", "Swimming Pool", "Spa", "Airport Shuttle"],
                source='booking_com'
            ))
        return results
