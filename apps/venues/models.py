from django.db import models
from apps.users.models import CustomUser  # Import CustomUser for owner relationship


class Venue(models.Model):
    """
    Model representing a venue for booking.
    Stores venue details such as name, location, pricing, and availability.
    """

    # Venue name (e.g., Grand Ballroom, Luxury Hall)
    name = models.CharField(
        max_length=255,
        verbose_name="Venue Name",
        help_text="The name of the venue."
    )

    # Location of the venue (City and State combined)
    location = models.CharField(
        max_length=255,
        verbose_name="Location",
        help_text="The location of the venue (e.g., New York, CA)."
    )

    # Full address of the venue
    address = models.TextField(
        verbose_name="Venue Address",
        help_text="The complete address of the venue."
    )

    # Price for the venue (general price or pricing based on duration)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="The general price for booking the venue."
    )

    # Maximum capacity of the venue (e.g., how many people it can hold)
    capacity = models.PositiveIntegerField(
        verbose_name="Capacity",
        help_text="The maximum number of people the venue can accommodate."
    )

    # Working hours of the venue (e.g., from 9:00 AM to 9:00 PM)
    working_hours = models.CharField(
        max_length=100,
        verbose_name="Working Hours",
        help_text="Working hours of the venue (e.g., 9:00 AM - 9:00 PM)."
    )

    # Dates when the venue is available for booking
    available_dates = models.TextField(
        verbose_name="Available Dates",
        help_text="Comma separated list of available dates for booking (e.g., '2023-12-01,2023-12-02')."
    )

    # Venue images (one or more images to represent the venue)
    image = models.ImageField(
        upload_to='venue_images/',  # Images will be stored in media/venue_images/
        blank=True,
        null=True,
        verbose_name="Venue Image",
        help_text="An optional image representing the venue."
    )

    # A brief description of the venue (optional)
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="A short description of the venue, e.g., its features or capacity."
    )

    # Owner of the venue (admin user)
    owner = models.ForeignKey(
        CustomUser,  # Foreign key to the custom user model
        on_delete=models.CASCADE,  # If the user is deleted, their venues are deleted
        related_name="venues",  # Related name for reverse querying
        verbose_name="Owner",
        help_text="The owner of the venue (admin user)."
    )

    # Availability status of the venue (whether it is available for booking)
    is_available = models.BooleanField(
        default=True,
        verbose_name="Availability",
        help_text="Indicates whether the venue is available for booking."
    )

    # Discount percentage (if any) applicable for bookings
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name="Discount",
        help_text="Discount percentage applicable for bookings. E.g., 10 for 10% discount."
    )

    # Timestamp for when the venue was created
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The timestamp when the venue was created."
    )

    # Timestamp for when the venue was last updated
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="The timestamp when the venue was last updated."
    )

    def __str__(self):
        """
        String representation of the venue object.
        """
        return self.name

    def calculate_booking_price(self, duration_in_hours):
        """
        Calculate the total price for booking the venue.
        :param duration_in_hours: Duration of the booking in hours
        :return: Total price for the booking
        """
        price = self.price

        # Apply discount if available
        if self.discount > 0:
            price = price - (price * self.discount / 100)

        if duration_in_hours >= 24:
            # Calculate based on daily pricing (if booking is more than 24 hours)
            days = -(-duration_in_hours // 24)  # Round up to the nearest day
            return price * days
        else:
            # Calculate based on hourly pricing
            return price * duration_in_hours

    class Meta:
        """
        Meta class provides additional options for the Venue model.
        """
        verbose_name = "Venue"
        verbose_name_plural = "Venues"
        ordering = ['-created_at']  # Default ordering by created timestamp (newest first)
