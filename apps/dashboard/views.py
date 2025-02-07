from datetime import datetime, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import CustomUser
from apps.book.models import Booking
from apps.book.serializers import BookingSerializer
from .permissions import IsAdminOrSuperAdmin, ReadOnly

# -------------------- Dashboard API --------------------

@api_view(['GET'])
@permission_classes([IsAdminOrSuperAdmin])
def dashboard(request):
    """
    Returns overall statistics for the dashboard:
    - Total users
    - Total orders
    - Total sales
    - Total pending orders
    """
    
    # 1. Total Users
    total_users = CustomUser.objects.count()

    # 2. Total Orders (Bookings)
    total_orders = Booking.objects.count()

    # 3. Total Sales (sum of total_price for all bookings)
    total_sales = Booking.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0

    # 4. Total Pending Orders
    total_pending = Booking.objects.filter(status='pending').count()

    # 5. Users this week (Users created this week)
    start_of_week = datetime.now() - timedelta(days=datetime.now().weekday())  # Start of the current week
    end_of_week = start_of_week + timedelta(days=7)
    users_this_week = CustomUser.objects.filter(date_joined__gte=start_of_week, date_joined__lte=end_of_week).count()

    # Return statistics
    statistics = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_sales': total_sales,
        'total_pending': total_pending,
        'users_this_week': users_this_week
    }
    return Response(statistics, status=status.HTTP_200_OK)


# -------------------- Booking Details API --------------------

@api_view(['GET'])
@permission_classes([IsAdminOrSuperAdmin])
def booking_details(request):
    """
    Returns all booking details or filters bookings by month and year.
    """
    # Get the filter parameters (default to the current month and year)
    month = request.query_params.get('month', datetime.now().month)
    year = request.query_params.get('year', datetime.now().year)

    # Filter bookings for the given month and year
    bookings = Booking.objects.filter(
        start_time__month=month,
        start_time__year=year
    ).order_by('start_time')

    # Serialize the bookings
    serializer = BookingSerializer(bookings, many=True)

    # Return the booking details
    return Response(serializer.data, status=status.HTTP_200_OK)
