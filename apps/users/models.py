# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Role(models.Model):
    """Role model for user roles."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    Includes a ForeignKey to Role and resolves reverse accessor conflicts with `groups` and `user_permissions`.
    """
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    groups = models.ManyToManyField(
        Group, related_name="custom_user_set", blank=True  # Avoid reverse accessor clashes
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_set", blank=True  # Avoid reverse accessor clashes
    )

    def __str__(self):
        return self.username