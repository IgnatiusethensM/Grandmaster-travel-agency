from django.contrib import admin
from .models import Hotel, RoomType

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomTypeInline]
    list_display = ('name', 'location', 'stars', 'price_per_night')
    list_filter = ('stars', 'location')
    search_fields = ('name', 'location')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hotel, HotelAdmin)
