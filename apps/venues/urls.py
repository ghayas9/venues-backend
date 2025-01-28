from django.urls import path
from .views import (
    list_admin_venues, create_venue, manage_venue,
    list_public_venues, retrieve_public_venue
)

urlpatterns = [
    # -------------------- Admin Endpoints --------------------
    path('admin/', list_admin_venues, name='list-admin-venues'),
    # Admins and super admins can list their own venues (or all venues for super admins).

    path('admin/create/', create_venue, name='create-venue'),
    # Admins and super admins can create new venues.

    path('admin/<int:venue_id>/', manage_venue, name='manage-venue'),
    # Admins and super admins can retrieve, update, or delete a specific venue.
    # Admins can only manage their own venues.

    # -------------------- Public Endpoints --------------------
    path('', list_public_venues, name='list-public-venues'),
    # Public endpoint to list all available venues (is_available=True).

    path('<int:venue_id>/', retrieve_public_venue, name='retrieve-public-venue'),
    # Public endpoint to retrieve details of a specific venue (is_available=True).
]
