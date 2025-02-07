from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.
    Provides tools for managing bookings, including searching, filtering, and customizing displayed fields.
    """

    # Fields to display in the admin list view
    list_display = [
        'id', 'book', 'venue', 'user', 'start_time', 'end_time', 'total_price', 
        'payment_status', 'status', 'created_at'
    ]

    # Fields to filter the list view
    list_filter = ['venue', 'payment_status', 'status', 'user']

    # Fields to search in the admin list view
    search_fields = ['book', 'venue__name', 'user__username', 'status']

    # Fields to display when editing or creating a booking
    fields = [
        'book', 'venue', 'user', 'start_time', 'end_time', 'total_price', 
        'payment_status', 'status'
    ]

    # Read-only fields in the admin panel (cannot be edited)
    readonly_fields = ['created_at', 'updated_at']

    # Ordering of the list view (default by creation date, descending)
    ordering = ['-created_at']
