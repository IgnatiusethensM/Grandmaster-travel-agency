from django.contrib import admin
from .models import Category, Destination, Package, PackageImage

class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 1

class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageImageInline]
    list_display = ('title', 'destination', 'category', 'price', 'duration_days', 'is_featured')
    list_filter = ('destination', 'category', 'is_featured')
    search_fields = ('title', 'destination__name')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
