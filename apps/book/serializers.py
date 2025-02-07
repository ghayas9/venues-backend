from rest_framework import serializers
from .models import Booking
from apps.venues.models import Venue
from apps.users.models import CustomUser

from apps.users.serializers import UserSerializer 
from apps.venues.serializers import VenueSerializer


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing Booking instances. Includes all fields such as venue, user, date, and price.
    """
    venue = VenueSerializer()  # Display venue name instead of ID
    user = UserSerializer()  # Display user (customer) username instead of ID
    created_at = serializers.DateTimeField(read_only=True)  # Read-only timestamp for when the booking was created
    updated_at = serializers.DateTimeField(read_only=True)  # Read-only timestamp for last update

    class Meta:
        model = Booking
        fields = [
            'id', 'book', 'venue', 'user', 'start_time', 'end_time', 'total_price',
            'payment_status', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'venue', 'user', 'created_at', 'updated_at']


class BookingCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating or updating Booking instances.
    """
    class Meta:
        model = Booking
        fields = [
            'book', 'venue', 'user', 'start_time', 'end_time', 'total_price', 
            'payment_status', 'status'
        ]
