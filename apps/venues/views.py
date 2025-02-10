# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from drf_yasg.utils import swagger_auto_schema
# from .models import Venue
# from .serializers import VenueSerializer, VenueCreateUpdateSerializer
# from .permissions import IsAdminOrSuperAdmin, ReadOnly
# from .swagger import (
#     list_admin_venues_swagger, create_venue_swagger,
#     manage_venue_swagger, list_public_venues_swagger,
#     retrieve_public_venue_swagger
# )


# # -------------------- Admin Endpoints --------------------

# @list_admin_venues_swagger
# @api_view(['GET'])
# @permission_classes([IsAdminOrSuperAdmin])
# def list_admin_venues(request):
#     """
#     Admin endpoint to list all venues.
#     - Admins: Can only see their own venues.
#     - Super Admins: Can see all venues.
#     """
#     if request.user.role == 'super_admin':
#         venues = Venue.objects.all()  # Super admin can see all venues
#     else:
#         venues = Venue.objects.filter(owner=request.user)  # Admins can only see their venues
#     serializer = VenueSerializer(venues, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @create_venue_swagger
# @api_view(['POST'])
# @permission_classes([IsAdminOrSuperAdmin])
# def create_venue(request):
#     """
#     Admin endpoint to create a new venue.
#     - Only accessible to admin and super admin users.
#     """
#     serializer = VenueCreateUpdateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(owner=request.user)  # Assign the logged-in user as the owner
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAdminOrSuperAdmin])
# def manage_venue(request, venue_id):
#     """
#     Admin endpoint to retrieve, update, or delete a specific venue.
#     - Admins: Can only manage their own venues.
#     - Super Admins: Can manage all venues.
#     """
#     if request.user.role == 'super_admin':
#         # Super Admins can access all venues
#         venue = get_object_or_404(Venue, id=venue_id)
#     else:
#         # Admins can only access their own venues
#         venue = get_object_or_404(Venue, id=venue_id, owner=request.user)

#     if request.method == 'GET':
#         # Retrieve venue details
#         serializer = VenueSerializer(venue)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         # Update venue details
#         serializer = VenueCreateUpdateSerializer(venue, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # Delete the venue
#         venue.delete()
#         return Response({"message": "Venue deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# # -------------------- Public Endpoints --------------------

# @list_public_venues_swagger
# @api_view(['GET'])
# @permission_classes([ReadOnly])
# def list_public_venues(request):
#     """
#     Public endpoint to list all available venues.
#     - No authentication required.
#     """
#     venues = Venue.objects.filter(is_available=True)  # Only show available venues
#     serializer = VenueSerializer(venues, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @retrieve_public_venue_swagger
# @api_view(['GET'])
# @permission_classes([ReadOnly])
# def retrieve_public_venue(request, venue_id):
#     """
#     Public endpoint to retrieve details of a specific venue.
#     - No authentication required.
#     """
#     venue = get_object_or_404(Venue, id=venue_id, is_available=True)
#     serializer = VenueSerializer(venue)
#     return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Venue
from .serializers import VenueSerializer, VenueCreateUpdateSerializer
from .permissions import IsAdminOrSuperAdmin, ReadOnly
from .swagger import (
    list_admin_venues_swagger, create_venue_swagger,
    manage_venue_swagger, list_public_venues_swagger,
    retrieve_public_venue_swagger
)


# -------------------- Admin Endpoints --------------------

@list_admin_venues_swagger
@api_view(['GET'])
@permission_classes([IsAdminOrSuperAdmin])
def list_admin_venues(request):
    """
    Admin endpoint to list all venues owned by the logged-in admin user.
    - Admins: Can only see their own venues.
    - Super Admins: Can see all venues across all admins.
    """
    if request.user.role == 'super_admin':
        venues = Venue.objects.all()  # Super admins can see all venues
    else:
        venues = Venue.objects.filter(owner=request.user)  # Admins can only see their venues
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@create_venue_swagger
@api_view(['POST'])
@permission_classes([IsAdminOrSuperAdmin])
def create_venue(request):
    """
    Admin endpoint to create a new venue.
    - Only accessible to admin and super admin users.
    """
    serializer = VenueCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)  # Assign the logged-in user as the venue owner
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrSuperAdmin])
def manage_venue(request, venue_id):
    """
    Admin endpoint to retrieve, update, or delete a specific venue owned by the logged-in admin user.
    - Admins: Can only manage their own venues.
    - Super Admins: Can manage all venues across all admins.
    """
    # Check if the user is a super admin or an admin for their own venue
    if request.user.role == 'super_admin':
        # Super Admins can access all venues
        venue = get_object_or_404(Venue, id=venue_id)
    else:
        # Admins can only access their own venues
        venue = get_object_or_404(Venue, id=venue_id, owner=request.user)

    # Handle different HTTP methods (GET, PUT, DELETE)
    if request.method == 'GET':
        # Retrieve venue details
        serializer = VenueSerializer(venue)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # Update venue details
        serializer = VenueCreateUpdateSerializer(venue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the venue
        venue.delete()
        return Response({"message": "Venue deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# -------------------- Public Endpoints --------------------

@list_public_venues_swagger
@api_view(['GET'])
@permission_classes([AllowAny])
def list_public_venues(request):
    """
    Public endpoint to list all available venues.
    - No authentication required.
    - Filters out venues that are not available.
    """
    venues = Venue.objects.filter(is_available=True)  # Only show available venues
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@retrieve_public_venue_swagger
@api_view(['GET'])
@permission_classes([AllowAny])
def retrieve_public_venue(request, venue_id):
    """
    Public endpoint to retrieve details of a specific venue.
    - No authentication required.
    - Only retrieves venues that are available.
    """
    venue = get_object_or_404(Venue, id=venue_id, is_available=True)
    serializer = VenueSerializer(venue)
    return Response(serializer.data, status=status.HTTP_200_OK)
