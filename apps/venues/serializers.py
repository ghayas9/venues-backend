from rest_framework import serializers
from .models import Venue


class VenueSerializer(serializers.ModelSerializer):
    """
    Serializer for the Venue model.
    Includes pricing information and other venue details.
    """
    owner = serializers.StringRelatedField(read_only=True)  # Display owner's username

    class Meta:
        model = Venue
        fields = [
            'id', 'name', 'address', 'city', 'state', 'zip_code',
            'description', 'capacity', 'image', 'hourly_price', 'daily_price',
            'owner', 'is_available', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']


class VenueCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Venue instances.
    """
    class Meta:
        model = Venue
        fields = [
            'name', 'address', 'city', 'state', 'zip_code', 'description',
            'capacity', 'image', 'hourly_price', 'daily_price', 'is_available'
        ]
