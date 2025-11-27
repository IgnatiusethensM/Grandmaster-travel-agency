from django.db import models
from django.utils.text import slugify

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    location = models.CharField(max_length=200)
    stars = models.PositiveIntegerField(default=3)
    amenities = models.JSONField(default=list)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hotels/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Additional cost per night")
    
    def __str__(self):
        return f"{self.name} at {self.hotel.name}"
