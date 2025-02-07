from django.urls import path
from . import views

urlpatterns = [
    # Dashboard API endpoint (overall statistics)
    path('', views.dashboard, name='dashboard'),

    # Booking details with optional filters for month and year
    path('book', views.booking_details, name='booking-details'),
]
