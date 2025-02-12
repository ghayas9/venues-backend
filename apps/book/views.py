# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import Booking
# from .serializers import BookingSerializer, BookingCreateUpdateSerializer
# from .swagger import (
#     list_bookings_swagger, create_booking_swagger,
#     manage_booking_swagger
# )
# from .permissions import IsAdminOrSuperAdmin, ReadOnly

# # -------------------- Admin Endpoints --------------------

# @list_bookings_swagger
# @api_view(['GET'])
# @permission_classes([IsAdminOrSuperAdmin])
# def list_bookings(request):
#     """
#     Admin endpoint to list all bookings.
#     - Admins: Can see all bookings for their own venues.
#     - Super Admins: Can see all bookings across all venues and users.
#     """
#     if request.user.role == 'super_admin':
#         bookings = Booking.objects.all()  # Super admin can see all bookings
#     else:
#         bookings = Booking.objects.filter(venue__owner=request.user)  # Admins can see only their own bookings
#     serializer = BookingSerializer(bookings, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @create_booking_swagger
# @api_view(['POST'])
# @permission_classes([IsAdminOrSuperAdmin])
# def create_booking(request):
#     """
#     Admin endpoint to create a new booking.
#     - Only accessible to admin and super admin users.
#     """
#     serializer = BookingCreateUpdateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)  # Assign the logged-in user as the user for the booking
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @manage_booking_swagger
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAdminOrSuperAdmin])
# def manage_booking(request, booking_id):
#     """
#     Admin endpoint to retrieve, update, or delete a specific booking.
#     - Admins: Can only manage bookings for their own venues.
#     - Super Admins: Can manage all bookings.
#     """
#     booking = get_object_or_404(Booking, id=booking_id)

#     if request.user.role != 'super_admin' and booking.venue.owner != request.user:
#         return Response({"error": "You do not have permission to manage this booking."}, status=status.HTTP_403_FORBIDDEN)

#     if request.method == 'GET':
#         # Retrieve booking details
#         serializer = BookingSerializer(booking)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         # Update booking details
#         serializer = BookingCreateUpdateSerializer(booking, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # Delete the booking
#         booking.delete()
#         return Response({"message": "Booking deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# # -------------------- Public Endpoints --------------------

# @list_bookings_swagger
# @api_view(['GET'])
# @permission_classes([ReadOnly])
# def public_list_bookings(request):
#     """
#     Public endpoint to list all available bookings.
#     - No authentication required.
#     """
#     bookings = Booking.objects.filter(status='confirmed')  # Only show confirmed bookings
#     serializer = BookingSerializer(bookings, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @manage_booking_swagger
# @api_view(['GET'])
# @permission_classes([ReadOnly])
# def public_retrieve_booking(request, booking_id):
#     """
#     Public endpoint to retrieve details of a specific booking.
#     - No authentication required.
#     """
#     booking = get_object_or_404(Booking, id=booking_id, status='confirmed')
#     serializer = BookingSerializer(booking)
#     return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Booking
from .serializers import BookingSerializer, BookingCreateUpdateSerializer
from .permissions import IsAdminOrSuperAdmin, ReadOnly
from .swagger import (
    list_bookings_swagger, create_booking_swagger,
    retrieve_booking_swagger, update_booking_swagger,
    delete_booking_swagger
)

# -------------------- Admin Endpoints --------------------

@list_bookings_swagger
@api_view(['GET'])
@permission_classes([IsAdminOrSuperAdmin])
def list_bookings(request):
    """
    Admin endpoint to list all bookings.
    - Customer: Can see all bookings for their own booking.
    - Admins: Can see all bookings for their own venues.
    - Super Admins: Can see all bookings across all venues and users.
    """
    # If user is super admin, return all bookings
    if request.user.role == 'super_admin':
        bookings = Booking.objects.all()
    # If user is an admin, return bookings for their venues
    elif request.user.role == 'admin':
        bookings = Booking.objects.filter(venue__owner=request.user)
    # If user is a customer, return only their bookings
    elif request.user.role == 'customer':
        bookings = Booking.objects.filter(user=request.user)
    else:
        return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    # Serialize the bookings data and return response
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@create_booking_swagger
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    """
    Admin endpoint to create a new booking.
    - Only accessible to admin and super admin users.
    """
    serializer = BookingCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@retrieve_booking_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_booking(request, booking_id):
    """
    Admin endpoint to retrieve details of a specific booking.
    - Admins: Can only manage bookings for their own venues.
    - Super Admins: Can manage all bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)


@update_booking_swagger
@api_view(['PUT'])
@permission_classes([IsAdminOrSuperAdmin])
def update_booking(request, booking_id):
    """
    Admin endpoint to update a specific booking.
    - Admins: Can only manage bookings for their own venues.
    - Super Admins: Can manage all bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    serializer = BookingCreateUpdateSerializer(booking, data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@delete_booking_swagger
@api_view(['DELETE'])
@permission_classes([IsAdminOrSuperAdmin])
def delete_booking(request, booking_id):
    """
    Admin endpoint to delete a specific booking.
    - Admins: Can only delete bookings for their own venues.
    - Super Admins: Can delete all bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return Response({"message": "Booking deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# -------------------- Public Endpoints --------------------

@list_bookings_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def public_list_bookings(request):
    """
    Public endpoint to list all available bookings.
    - No authentication required.
    """
    bookings = Booking.objects.filter(status='confirmed')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@retrieve_booking_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def public_retrieve_booking(request, booking_id):
    """
    Public endpoint to retrieve details of a specific booking.
    - No authentication required.
    """
    booking = get_object_or_404(Booking, id=booking_id, status='confirmed')
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)
