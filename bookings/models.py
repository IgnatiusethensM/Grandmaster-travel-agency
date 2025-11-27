from django.db import models
from django.conf import settings
from packages.models import Package
from hotels.models import Hotel

class Booking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('UNPAID', 'Unpaid'),
        ('PARTIAL', 'Partial'),
        ('PAID', 'Paid'),
        ('REFUNDED', 'Refunded'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)
    
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    special_requests = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='UNPAID')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for Booking #{self.booking.id}"
