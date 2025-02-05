# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from .serializers import VenueSerializer, VenueCreateUpdateSerializer

# # ------------------ Swagger Schemas ------------------

# # Request body schema for creating or updating a venue
# venue_request_body = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the venue"),
#         'address': openapi.Schema(type=openapi.TYPE_STRING, description="Address of the venue"),
#         'city': openapi.Schema(type=openapi.TYPE_STRING, description="City where the venue is located"),
#         'state': openapi.Schema(type=openapi.TYPE_STRING, description="State where the venue is located"),
#         'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description="Zip code of the venue"),
#         'description': openapi.Schema(type=openapi.TYPE_STRING, description="Description of the venue (optional)"),
#         'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Capacity of the venue"),
#         'hourly_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Hourly price for booking the venue"),
#         'daily_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Daily price for booking the venue"),
#         'image': openapi.Schema(type=openapi.TYPE_STRING, format="binary", description="Image of the venue (optional)"),
#         'is_available': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Availability status of the venue"),
#     },
#     required=['name', 'address', 'city', 'state', 'zip_code', 'capacity', 'hourly_price', 'daily_price', 'is_available']
# )

# # Response schema for venue details
# venue_response = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the venue"),
#         'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the venue"),
#         'address': openapi.Schema(type=openapi.TYPE_STRING, description="Address of the venue"),
#         'city': openapi.Schema(type=openapi.TYPE_STRING, description="City of the venue"),
#         'state': openapi.Schema(type=openapi.TYPE_STRING, description="State of the venue"),
#         'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description="Zip code of the venue"),
#         'description': openapi.Schema(type=openapi.TYPE_STRING, description="Description of the venue"),
#         'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Capacity of the venue"),
#         'hourly_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Hourly price"),
#         'daily_price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Daily price"),
#         'image': openapi.Schema(type=openapi.TYPE_STRING, description="Image URL of the venue"),
#         'is_available': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Availability status"),
#         'owner': openapi.Schema(type=openapi.TYPE_STRING, description="Owner of the venue"),
#         'created_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Creation timestamp"),
#         'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Last update timestamp"),
#     }
# )

# # ------------------ Swagger Annotations ------------------

# # Swagger for listing all admin-owned venues
# list_admin_venues_swagger = swagger_auto_schema(
#     method='get',
#     operation_description="List all venues owned by the logged-in admin user.",
#     responses={
#         200: VenueSerializer(many=True),
#         403: "Forbidden - Access denied",
#     }
# )

# # Swagger for creating a venue
# create_venue_swagger = swagger_auto_schema(
#     method='post',
#     operation_description="Create a new venue owned by the logged-in admin user. Includes pricing information.",
#     request_body=venue_request_body,
#     responses={
#         201: venue_response,
#         400: "Validation errors",
#         403: "Forbidden - Access denied",
#     }
# )

# # Swagger for retrieving, updating, or deleting a venue
# manage_venue_swagger = {
#     'get': swagger_auto_schema(
#         operation_description="Retrieve details of a specific venue owned by the logged-in admin user.",
#         responses={
#             200: venue_response,
#             404: "Not Found - Venue not found or access denied",
#         }
#     ),
#     'put': swagger_auto_schema(
#         operation_description="Update details of a specific venue owned by the logged-in admin user.",
#         request_body=venue_request_body,
#         responses={
#             200: venue_response,
#             400: "Validation errors",
#             404: "Not Found - Venue not found or access denied",
#         }
#     ),
#     'delete': swagger_auto_schema(
#         operation_description="Delete a specific venue owned by the logged-in admin user.",
#         responses={
#             204: "No Content - Venue deleted successfully",
#             404: "Not Found - Venue not found or access denied",
#         }
#     ),
# }

# # Swagger for listing all public venues
# list_public_venues_swagger = swagger_auto_schema(
#     method='get',
#     operation_description="List all available public venues. No authentication required.",
#     responses={200: VenueSerializer(many=True)}
# )

# # Swagger for retrieving a specific public venue
# retrieve_public_venue_swagger = swagger_auto_schema(
#     method='get',
#     operation_description="Retrieve details of a specific public venue. No authentication required.",
#     responses={
#         200: venue_response,
#         404: "Not Found - Venue not found or not available",
#     }
# )



from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import VenueSerializer, VenueCreateUpdateSerializer

# ------------------ Swagger Schemas ------------------

# Request body schema for creating or updating a venue
venue_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the venue"),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description="Location of the venue (e.g., 'New York, CA')"),
        'address': openapi.Schema(type=openapi.TYPE_STRING, description="Address of the venue"),
        'price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Base price for booking the venue"),
        'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Maximum capacity of the venue"),
        'working_hours': openapi.Schema(type=openapi.TYPE_STRING, description="Working hours of the venue (e.g., '9:00 AM - 9:00 PM')"),
        'available_dates': openapi.Schema(type=openapi.TYPE_STRING, description="Comma separated list of available dates for booking (e.g., '2023-12-01,2023-12-02')"),
        'image': openapi.Schema(type=openapi.TYPE_STRING, format="binary", description="Image of the venue (optional)"),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description="Description of the venue (optional)"),
        'is_available': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Availability status of the venue"),
        'discount': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Discount percentage for the venue booking"),
    },
    required=['name', 'location', 'address', 'price', 'capacity', 'working_hours', 'available_dates', 'is_available']
)

# Response schema for venue details
venue_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the venue"),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the venue"),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description="Location of the venue"),
        'address': openapi.Schema(type=openapi.TYPE_STRING, description="Address of the venue"),
        'price': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Price for booking the venue"),
        'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Maximum capacity of the venue"),
        'working_hours': openapi.Schema(type=openapi.TYPE_STRING, description="Working hours of the venue"),
        'available_dates': openapi.Schema(type=openapi.TYPE_STRING, description="Available dates for booking the venue"),
        'image': openapi.Schema(type=openapi.TYPE_STRING, description="Image URL of the venue"),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description="Description of the venue"),
        'is_available': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Availability status of the venue"),
        'discount': openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Discount percentage for booking"),
        'owner': openapi.Schema(type=openapi.TYPE_STRING, description="Owner of the venue"),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Creation timestamp"),
        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description="Last update timestamp"),
    }
)

# ------------------ Swagger Annotations ------------------

# Swagger for listing all admin-owned venues
list_admin_venues_swagger = swagger_auto_schema(
    method='get',
    operation_description="List all venues owned by the logged-in admin user.",
    responses={
        200: VenueSerializer(many=True),
        403: "Forbidden - Access denied",
    }
)

# Swagger for creating a venue
create_venue_swagger = swagger_auto_schema(
    method='post',
    operation_description="Create a new venue owned by the logged-in admin user. Includes pricing information.",
    request_body=venue_request_body,
    responses={
        201: venue_response,
        400: "Validation errors",
        403: "Forbidden - Access denied",
    }
)

# Swagger for retrieving, updating, or deleting a venue
manage_venue_swagger = {
    'get': swagger_auto_schema(
        operation_description="Retrieve details of a specific venue owned by the logged-in admin user.",
        responses={
            200: venue_response,
            404: "Not Found - Venue not found or access denied",
        }
    ),
    'put': swagger_auto_schema(
        operation_description="Update details of a specific venue owned by the logged-in admin user.",
        request_body=venue_request_body,
        responses={
            200: venue_response,
            400: "Validation errors",
            404: "Not Found - Venue not found or access denied",
        }
    ),
    'delete': swagger_auto_schema(
        operation_description="Delete a specific venue owned by the logged-in admin user.",
        responses={
            204: "No Content - Venue deleted successfully",
            404: "Not Found - Venue not found or access denied",
        }
    ),
}

# Swagger for listing all public venues
list_public_venues_swagger = swagger_auto_schema(
    method='get',
    operation_description="List all available public venues. No authentication required.",
    responses={200: VenueSerializer(many=True)}
)

# Swagger for retrieving a specific public venue
retrieve_public_venue_swagger = swagger_auto_schema(
    method='get',
    operation_description="Retrieve details of a specific public venue. No authentication required.",
    responses={
        200: venue_response,
        404: "Not Found - Venue not found or not available",
    }
)
