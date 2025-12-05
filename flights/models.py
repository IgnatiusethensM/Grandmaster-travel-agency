from django.db import models
from bookings.models import Booking

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Airline(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    logo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Scheduled')

    def __str__(self):
        return f"{self.airline.code}{self.flight_number} - {self.origin.code} to {self.destination.code}"

    @property
    def duration(self):
        return self.arrival_time - self.departure_time

class FlightBooking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='flight_booking')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return f"Booking {self.booking.id} - {self.passenger_name}"
