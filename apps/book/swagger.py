from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import BookingSerializer, BookingCreateUpdateSerializer

# ------------------ Swagger Schemas ------------------

# Request body schema for creating or updating a booking
booking_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'book': openapi.Schema(type=openapi.TYPE_STRING, description="Booking reference"),
        'venue': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the venue being booked"),
        'user': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the user who made the booking"),
        'start_time': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Booking start time"),
        'end_time': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Booking end time"),
        'total_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Total price for the booking"),
        'payment_status': openapi.Schema(type=openapi.TYPE_STRING, description="Payment status of the booking"),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description="Booking status (e.g., confirmed, cancelled)"),
    },
    required=['book', 'venue', 'user', 'start_time', 'end_time', 'total_price', 'payment_status', 'status']
)

# Response schema for booking details
booking_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the booking"),
        'book': openapi.Schema(type=openapi.TYPE_STRING, description="Booking reference"),
        'venue': openapi.Schema(type=openapi.TYPE_STRING, description="Venue name"),
        'user': openapi.Schema(type=openapi.TYPE_STRING, description="User username"),
        'start_time': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Booking start time"),
        'end_time': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Booking end time"),
        'total_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Total price for the booking"),
        'payment_status': openapi.Schema(type=openapi.TYPE_STRING, description="Payment status of the booking"),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description="Booking status (e.g., confirmed, cancelled)"),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Creation timestamp"),
        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Last update timestamp"),
    }
)

# ------------------ Swagger Annotations ------------------

# Swagger for listing all bookings
list_bookings_swagger = swagger_auto_schema(
    method='get',
    operation_description="List all bookings for the logged-in user.",
    responses={200: BookingSerializer(many=True)}
)

# Swagger for creating a booking
create_booking_swagger = swagger_auto_schema(
    method='post',
    operation_description="Create a new booking.",
    request_body=booking_request_body,
    responses={201: booking_response, 400: "Bad Request"}
)

# Swagger for retrieving a specific booking
retrieve_booking_swagger = swagger_auto_schema(
    method='get',
    operation_description="Retrieve details of a specific booking.",
    responses={200: booking_response, 404: "Not Found"}
)

# Swagger for updating a booking
update_booking_swagger = swagger_auto_schema(
    method='put',
    operation_description="Update a specific booking.",
    request_body=booking_request_body,
    responses={200: booking_response, 400: "Bad Request", 404: "Not Found"}
)

# Swagger for deleting a booking
delete_booking_swagger = swagger_auto_schema(
    method='delete',
    operation_description="Delete a specific booking.",
    responses={204: "No Content", 404: "Not Found"}
)
