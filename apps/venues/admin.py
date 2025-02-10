# from django.contrib import admin
# from .models import Venue


# @admin.register(Venue)
# class VenueAdmin(admin.ModelAdmin):
#     """
#     Admin configuration for the Venue model.
#     Provides tools for managing venues, including searching, filtering, and customizing displayed fields.
#     """

#     # Fields to display in the admin list view
#     list_display = [
#         'id', 'name', 'location', 'capacity', 'price', 'working_hours', 
#         'available_dates', 'is_available', 'owner', 'discount', 'created_at'
#     ]

#     # Fields to filter the list view
#     list_filter = ['location', 'is_available', 'owner', 'discount']

#     # Fields to search in the admin list view
#     search_fields = ['name', 'location', 'owner__username']

#     # Fields to display when editing or creating a venue
#     fields = [
#         'name', 'location', 'address', 'description',
#         'capacity', 'working_hours', 'available_dates', 'image', 'price',
#         'is_available', 'discount', 'owner'
#     ]

#     # Read-only fields in the admin panel (cannot be edited)
#     readonly_fields = ['created_at', 'updated_at']

#     # Ordering of the list view (default by creation date, descending)
#     ordering = ['-created_at']

#     def get_queryset(self, request):
#         """
#         Customizes the queryset for the admin panel.
#         For example, restrict displayed venues based on certain criteria.
#         """
#         qs = super().get_queryset(request)
#         # Example: Only show venues for the logged-in user if they are not superuser
#         if not request.user.is_superuser:
#             qs = qs.filter(owner=request.user)
#         return qs

#     def has_add_permission(self, request):
#         """
#         Controls whether the user has permission to add a new venue.
#         """
#         return request.user.is_superuser or request.user.role == 'admin'

#     def has_delete_permission(self, request, obj=None):
#         """
#         Controls whether the user has permission to delete a venue.
#         """
#         return request.user.is_superuser or (obj and obj.owner == request.user)

from django.contrib import admin
from .models import Venue
from apps.book.models import Booking  # Corrected import for Booking
from django.utils.html import mark_safe

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 1  # Number of extra forms to display by default

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Venue model.
    Provides tools for managing venues, including searching, filtering, and customizing displayed fields.
    """

    # Fields to display in the admin list view
    list_display = [
        'id', 'name', 'location', 'capacity', 'price', 'working_hours', 
        'available_dates', 'is_available', 'owner', 'discount', 'created_at', 'image_preview'
    ]

    # Fields to filter the list view
    list_filter = ['location', 'is_available', 'owner', 'discount']

    # Fields to search in the admin list view
    search_fields = ['name', 'location', 'owner__username']

    # Fields to display when editing or creating a venue
    fields = [
        'name', 'location', 'address', 'description',
        'capacity', 'working_hours', 'available_dates', 'image', 'price',
        'is_available', 'discount', 'owner'
    ]

    # Read-only fields in the admin panel (cannot be edited)
    readonly_fields = ['created_at', 'updated_at']

    # Ordering of the list view (default by creation date, descending)
    ordering = ['-created_at']

    # Inline for bookings associated with the venue
    inlines = [BookingInline]

    def get_queryset(self, request):
        """
        Customizes the queryset for the admin panel.
        For example, restrict displayed venues based on certain criteria.
        """
        qs = super().get_queryset(request)
        # Example: Only show venues for the logged-in user if they are not superuser
        if not request.user.is_superuser:
            qs = qs.filter(owner=request.user)
        return qs

    def has_add_permission(self, request):
        """
        Controls whether the user has permission to add a new venue.
        """
        return request.user.is_superuser or request.user.role == 'admin'

    def has_delete_permission(self, request, obj=None):
        """
        Controls whether the user has permission to delete a venue.
        """
        return request.user.is_superuser or (obj and obj.owner == request.user)

    def image_preview(self, obj):
        """
        Display a small thumbnail of the venue's image in the admin list view.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" />')
        return "No image"
    image_preview.short_description = 'Image Preview'
