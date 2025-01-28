from django.db import models
from apps.users.models import CustomUser


class Venue(models.Model):
    """
    Model representing a venue for booking.
    Stores venue details and pricing information.
    """

    # Basic venue details
    name = models.CharField(max_length=255, verbose_name="Venue Name", help_text="The name of the venue (e.g., Grand Ballroom).")
    address = models.TextField(verbose_name="Venue Address", help_text="The full address of the venue.")
    city = models.CharField(max_length=100, verbose_name="City", help_text="The city where the venue is located.")
    state = models.CharField(max_length=100, verbose_name="State", help_text="The state where the venue is located.")
    zip_code = models.CharField(max_length=10, verbose_name="Zip Code", help_text="The zip code for the venue's location.")
    description = models.TextField(blank=True, null=True, verbose_name="Description", help_text="A brief description of the venue.")
    capacity = models.PositiveIntegerField(verbose_name="Capacity", help_text="The maximum number of people the venue can accommodate.")
    image = models.ImageField(upload_to='venue_images/', blank=True, null=True, verbose_name="Venue Image", help_text="An optional image of the venue.")

    # Pricing fields
    hourly_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Hourly Price", help_text="Price for booking the venue per hour.")
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Daily Price", help_text="Price for booking the venue for a full day (24 hours).")

    # Ownership and availability
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="venues", verbose_name="Owner", help_text="The owner of the venue (admin user).")
    is_available = models.BooleanField(default=True, verbose_name="Availability", help_text="Indicates whether the venue is currently available for booking.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", help_text="The timestamp when the venue was created.")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At", help_text="The timestamp when the venue was last updated.")

    def __str__(self):
        """
        String representation of the venue object.
        """
        return self.name

    def calculate_booking_price(self, duration_in_hours):
        """
        Calculate the price for booking the venue.
        :param duration_in_hours: Duration of the booking in hours
        :return: Total price for the booking
        """
        if duration_in_hours >= 24:
            days = -(-duration_in_hours // 24)  # Round up to the nearest full day
            return self.daily_price * days
        return self.hourly_price * duration_in_hours

    class Meta:
        verbose_name = "Venue"
        verbose_name_plural = "Venues"
        ordering = ['-created_at']
