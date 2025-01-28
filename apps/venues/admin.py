from django.contrib import admin
from .models import Venue


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Venue model.
    Provides tools for managing venues, including searching, filtering, and customizing displayed fields.
    """

    # Fields to display in the admin list view
    list_display = [
        'id', 'name', 'city', 'state', 'capacity', 'hourly_price', 'daily_price',
        'is_available', 'owner', 'created_at'
    ]

    # Fields to filter the list view
    list_filter = ['city', 'state', 'is_available', 'owner']

    # Fields to search in the admin list view
    search_fields = ['name', 'city', 'state', 'owner__username']

    # Fields to display when editing or creating a venue
    fields = [
        'name', 'address', 'city', 'state', 'zip_code', 'description', 'capacity',
        'image', 'hourly_price', 'daily_price', 'is_available', 'owner'
    ]

    # Read-only fields in the admin panel (cannot be edited)
    readonly_fields = ['created_at', 'updated_at']

    # Ordering of the list view (default by creation date, descending)
    ordering = ['-created_at']

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
