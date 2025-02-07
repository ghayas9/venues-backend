from django.db import models
from apps.users.models import CustomUser
from apps.venues.models import Venue

class Booking(models.Model):
    """
    Model representing a booking for a venue.
    Stores the booking details such as venue, user, date, and pricing.
    """

    # The venue being booked
    venue = models.ForeignKey(
        Venue, 
        on_delete=models.CASCADE,  # If the venue is deleted, the booking is deleted
        related_name="bookings",
        verbose_name="Venue",
        help_text="The venue being booked."
    )

    # The user who made the booking (Customer)
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,  # If the user is deleted, the booking is deleted
        related_name="bookings",
        verbose_name="User",
        help_text="The user who made the booking."
    )

    # The date and time when the booking starts
    start_time = models.DateTimeField(
        verbose_name="Start Time",
        help_text="The date and time when the booking starts."
    )

    # The date and time when the booking ends
    end_time = models.DateTimeField(
        verbose_name="End Time",
        help_text="The date and time when the booking ends."
    )

    # Total price for the booking (calculated based on duration and venue pricing)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Price",
        help_text="The total price for the booking."
    )

    # Payment status (if the booking has been paid for)
    PAYMENT_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        default='pending',
        verbose_name="Payment Status",
        help_text="The payment status for this booking."
    )

    # Booking status (e.g., confirmed, cancelled)
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Booking Status",
        help_text="The status of the booking."
    )

    # Timestamp when the booking was created
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The timestamp when the booking was created."
    )

    # Timestamp when the booking was last updated
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="The timestamp when the booking was last updated."
    )

    # Replace the `name` field with `book` to store booking reference
    book = models.CharField(
        max_length=255,
        verbose_name="Booking Reference",
        help_text="A reference or name for the booking."
    )

    def __str__(self):
        """
        String representation of the booking object.
        """
        return f"Booking reference {self.book} for {self.venue.name} by {self.user.username} from {self.start_time} to {self.end_time}"

    def calculate_duration(self):
        """
        Calculate the duration of the booking in hours.
        """
        duration = self.end_time - self.start_time
        return duration.total_seconds() / 3600  # Return the duration in hours

    class Meta:
        """
        Meta class provides additional options for the Booking model.
        """
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-created_at']  # Default ordering by creation timestamp (newest first)
