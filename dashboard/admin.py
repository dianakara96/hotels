# dashboard/admin.py

from django.contrib import admin
from addhotel.models import addhotel  # Import Hotel from the hotels app
from myapp.models import CustomUser  # Import CustomUser from myapp

# Register the CustomUser model to view in the admin interface
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    fields = ('username', 'email', 'role')

# Register the Hotel model to view in the admin interface
@admin.register(addhotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'price')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    fields = ('name', 'description', 'location', 'price')
