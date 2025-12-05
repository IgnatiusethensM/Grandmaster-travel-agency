from django.db import models
from bookings.models import Booking

class VehicleType(models.Model):
    name = models.CharField(max_length=100) # e.g., Sedan, SUV, Van
    capacity = models.PositiveIntegerField()
    image = models.URLField(blank=True, null=True)
    base_rate = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TransferBooking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='transfer_booking')
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    pickup_time = models.DateTimeField()
    distance_km = models.DecimalField(max_digits=10, decimal_places=2, help_text="Estimated distance")
    flight_number = models.CharField(max_length=20, blank=True, null=True, help_text="For airport pickups")
    driver_note = models.TextField(blank=True)

    def __str__(self):
        return f"Transfer: {self.pickup_location} to {self.dropoff_location}"
