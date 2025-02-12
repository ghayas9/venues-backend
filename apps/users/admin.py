from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django.utils.html import mark_safe

class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for managing CustomUser models.
    Provides search, filter, and custom display options.
    """

    # Fields to display in the admin list view
    list_display = ['id','name', 'username', 'email', 'role', 'status', 'image_preview']

    # Fields to filter the list view by
    list_filter = ['role', 'status', 'is_active']

    # Fields to search in the admin list view
    search_fields = ['username', 'email', 'name']

    # Fields to display when editing or creating a user in the admin panel
    fields = (
        'username',
        'email',
        'name',
        'role',
        'status',
        'is_active',
        'image',  # Include image here
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
    )

    # Add image in add_fieldsets (for user creation)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'role', 'status', 'is_active', 'image', 'password1', 'password2'),
        }),
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
        # Example: You could filter by role or any other field
        return qs

    def has_add_permission(self, request):
        """
        Enable/disable adding users through the admin panel.
        Returning True enables adding users.
        """
        return True  # Change to False to disable adding users.

    def has_delete_permission(self, request, obj=None):
        """
        Control whether users can be deleted through the admin panel.
        Returning True allows deletion of users.
        """
        return True  # Change to False to disable deletion of users.

    def save_model(self, request, obj, form, change):
        """
        Handle user password securely in the admin form.
        Override the save method to ensure password hashing works properly.
        """
        
        if obj.pk is None: 
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
    def image_preview(self, obj):
        """
        Display a small thumbnail of the venue's image in the admin list view.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" />')
        return "No image"
    image_preview.short_description = 'Image Preview'

# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
