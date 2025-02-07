from datetime import datetime, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from apps.users.models import CustomUser
from apps.book.models import Booking
from .serializers import BookingSerializer
from .permissions import ReadOnly
from django.db.models import Sum

# -------------------- Dashboard API --------------------

@api_view(['GET'])
@permission_classes([ReadOnly])
def dashboard(request):
    """
    Returns overall statistics for the dashboard:
    - Total users
    - Total orders
    - Total sales
    - Total pending orders
    - Users created this week (as a graph)
    """
    
    # 1. Total Users
    total_users = CustomUser.objects.count() or 0

    # 2. Total Orders (Bookings)
    total_orders = Booking.objects.count() or 0

    # 3. Total Sales (sum of total_price for all bookings)
    total_sales = Booking.objects.aggregate(total_sales=Sum('total_price'))['total_sales'] or 0

    # 4. Total Pending Orders
    total_pending = Booking.objects.filter(status='pending').count() or 0

    # 5. Users created this week (for graph)
    start_of_week = datetime.now() - timedelta(days=datetime.now().weekday())  # Start of the current week
    end_of_week = start_of_week + timedelta(days=7)
    
    # Generate a list of the last 7 days (including today)
    days_of_week = [(start_of_week + timedelta(days=i)).date() for i in range(7)]  # List of dates for the week

    # Get users created during the current week, grouped by the date they were created
    user_data = CustomUser.objects.filter(date_joined__gte=start_of_week, date_joined__lte=end_of_week) \
        .extra(select={'day': 'date(date_joined)'}).values('day').annotate(user_count=Count('id')).order_by('day')

    # Prepare the data for graphing
    # Initialize empty lists for x_data and y_data
    x_data = days_of_week  # Dates for the last 7 days
    y_data = [0] * 7  # Initialize user count to 0 for each day

    # Map user data to the corresponding day
    for entry in user_data:
        # Convert entry['day'] to a date object for comparison with days_of_week
        entry_day = datetime.strptime(entry['day'], '%Y-%m-%d').date()
        if entry_day in days_of_week:
            day_index = days_of_week.index(entry_day)  # Find the index of the day
            y_data[day_index] = entry['user_count']  # Set the user count for the correct day

    # Return statistics along with user data for graph
    statistics = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_sales': total_sales,
        'total_pending': total_pending,
        'users_this_week_graph': {'x': [str(date) for date in x_data], 'y': y_data}  # Data for graph (dates vs user counts)
    }

    return Response(statistics, status=status.HTTP_200_OK)

# -------------------- Booking Details API --------------------

@api_view(['GET'])
@permission_classes([ReadOnly])
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
