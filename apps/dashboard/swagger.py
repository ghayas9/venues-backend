from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import BookingSerializer

# ------------------ Swagger Schemas ------------------

# Request body schema for filtering booking details
booking_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'month': openapi.Schema(type=openapi.TYPE_INTEGER, description="Month for filtering"),
        'year': openapi.Schema(type=openapi.TYPE_INTEGER, description="Year for filtering"),
    },
)

# Response schema for dashboard statistics
dashboard_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'total_users': openapi.Schema(type=openapi.TYPE_INTEGER, description="Total users"),
        'total_orders': openapi.Schema(type=openapi.TYPE_INTEGER, description="Total orders"),
        'total_sales': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Total sales"),
        'total_pending': openapi.Schema(type=openapi.TYPE_INTEGER, description="Total pending orders"),
        'users_this_week': openapi.Schema(type=openapi.TYPE_INTEGER, description="Users registered this week"),
    }
)

# Swagger for listing all dashboard statistics
dashboard_swagger = swagger_auto_schema(
    method='get',
    operation_description="Returns overall statistics for the dashboard",
    responses={200: dashboard_response}
)

# Swagger for booking details with month/year filtering
booking_details_swagger = swagger_auto_schema(
    method='get',
    operation_description="Returns booking details for a specific month and year",
    request_body=booking_request_body,
    responses={200: BookingSerializer(many=True), 400: "Bad Request"}
)
