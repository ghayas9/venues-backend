from rest_framework import serializers
from apps.book.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for booking details.
    """
    class Meta:
        model = Booking
        fields = [
            'id', 'book', 'venue', 'user', 'start_time', 'end_time', 'total_price',
            'payment_status', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
