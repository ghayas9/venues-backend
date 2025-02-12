from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """
    CustomUser model extends Django's AbstractUser to add custom fields 
    for our application's user management needs.
    """

    ROLE_CHOICES = [
        ('customer', 'Customer'),  # Regular customer
        ('admin', 'Admin'),        # Venue administrator
        ('super_admin', 'Super Admin'),  # Platform super admin
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('blocked', 'Blocked')
    ]

    # Custom fields
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer',
        help_text="Defines the role of the user: Customer, Admin, or Super Admin."
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Defines the status of the user: Pending, Active, or Block."
    )

    otp = models.IntegerField(
        null=True,
        blank=True,
        help_text="Stores the One-Time Password (OTP) for password reset functionality."
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Optional field to store the user's full name."
    )

    image = models.ImageField(
        upload_to='profile/',
        null=True,
        blank=True,
        help_text="Profile picture of the user."
    )

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups", 
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        """
        String representation of the user object.
        Returns the username or email for better identification in admin and debugging.
        """
        return self.username or self.email

    class Meta:
        """
        Meta class provides additional options for the CustomUser model.
        """
        verbose_name = "User"           # Singular name for the model
        verbose_name_plural = "Users"  # Plural name for the model
        ordering = ['-date_joined']    # Default ordering by date joined, descending

    def save(self, *args, **kwargs):
        """
        Override the save method to add any custom logic before saving the user object.
        """
        if not self.username and self.email:
            # If username is not provided, use the email as the username
            self.username = self.email
        super().save(*args, **kwargs)

