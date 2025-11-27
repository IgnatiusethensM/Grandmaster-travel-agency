from django.contrib import admin
from .models import Booking, Review

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'package', 'hotel', 'status', 'payment_status', 'total_price', 'created_at')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('user__username', 'user__email', 'id')
    readonly_fields = ('created_at', 'updated_at')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'user', 'rating', 'is_verified', 'created_at')
    list_filter = ('rating', 'is_verified')
    search_fields = ('user__username', 'comment')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
