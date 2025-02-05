# from rest_framework import serializers
# from .models import Venue


# class VenueSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the Venue model.
#     Includes pricing information and other venue details.
#     """
#     owner = serializers.StringRelatedField(read_only=True)  # Display owner's username

#     class Meta:
#         model = Venue
#         fields = [
#             'id', 'name', 'address', 'city', 'state', 'zip_code',
#             'description', 'capacity', 'image', 'hourly_price', 'daily_price',
#             'owner', 'is_available', 'created_at', 'updated_at'
#         ]
#         read_only_fields = ['id', 'owner', 'created_at', 'updated_at']


# class VenueCreateUpdateSerializer(serializers.ModelSerializer):
#     """
#     Serializer for creating and updating Venue instances.
#     """
#     class Meta:
#         model = Venue
#         fields = [
#             'name', 'address', 'city', 'state', 'zip_code', 'description',
#             'capacity', 'image', 'hourly_price', 'daily_price', 'is_available'
#         ]


from rest_framework import serializers
from .models import Venue

class VenueSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing Venue instances. Includes all fields like name, location, pricing, and owner.
    """
    owner = serializers.StringRelatedField(read_only=True)  # Display owner's username instead of the owner ID
    created_at = serializers.DateTimeField(read_only=True)  # Timestamp for when the venue was created
    updated_at = serializers.DateTimeField(read_only=True)  # Timestamp for when the venue was last updated

    class Meta:
        model = Venue
        fields = [
            'id', 'name', 'location', 'address', 'price', 'capacity', 'working_hours',
            'available_dates', 'image', 'description', 'owner', 'is_available', 'discount',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']  # Read-only fields

class VenueCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Venue instances.
    Allows the client to create or update venues.
    """
    class Meta:
        model = Venue
        fields = [
            'name', 'location', 'address', 'price', 'capacity', 'working_hours',
            'available_dates', 'image', 'description', 'is_available', 'discount'
        ]
