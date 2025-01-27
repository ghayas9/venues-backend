# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin for the User model.
    """
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'role')  # Fields displayed in admin list view
    list_filter = ('is_staff', 'is_superuser', 'role')  # Filters in the admin sidebar
    search_fields = ('username', 'email')  # Searchable fields

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    """
    Admin for the Role model.
    """
    list_display = ('id', 'name')  # Display role names in admin
    search_fields = ('name',)  # Allow searching roles by name