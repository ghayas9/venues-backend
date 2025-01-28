from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for managing CustomUser models.
    Provides search, filter, and custom display options.
    """
    # Fields to display in the admin list view
    list_display = ['id', 'username', 'email', 'role', 'is_approved', 'is_active']

    # Fields to filter the list view by
    list_filter = ['role', 'is_approved', 'is_active']

    # Fields to search in the admin list view
    search_fields = ['username', 'email', 'name']

    # Fields to display when editing or creating a user in the admin panel
    fields = (
        'username',
        'email',
        'name',
        'role',
        'is_approved',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
        'password',
    )

    # Read-only fields in the admin panel (non-editable)
    readonly_fields = ['date_joined', 'last_login']

    # Custom ordering of the list view
    ordering = ['-date_joined']

    def get_queryset(self, request):
        """
        Custom queryset to filter users based on specific criteria if needed.
        """
        qs = super().get_queryset(request)
        # You can customize this if necessary. For now, it shows all users.
        return qs

    def has_add_permission(self, request):
        """
        Disable adding new users through the admin panel if needed.
        Returning True enables adding users.
        """
        return True  # Change to False to disable adding users.

    def has_delete_permission(self, request, obj=None):
        """
        Control whether users can be deleted through the admin panel.
        """
        return True  # Change to False to disable deletion of users.
