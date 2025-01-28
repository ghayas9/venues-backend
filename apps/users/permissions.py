from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperAdmin(BasePermission):
    """
    Custom permission to grant access only to super admins.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the 'super_admin' role
        return request.user.is_authenticated and request.user.role == 'super_admin'


class IsAdminOrSuperAdmin(BasePermission):
    """
    Custom permission to grant access to both admins and super admins.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is either an admin or a super admin
        return request.user.is_authenticated and request.user.role in ['admin', 'super_admin']


class IsAdminAndOwner(BasePermission):
    """
    Custom permission to ensure the user is an admin and owns the resource.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated, is an admin, and is the owner of the object
        return (
            request.user.is_authenticated and
            request.user.role == 'admin' and
            obj.owner == request.user
        )


class ReadOnly(BasePermission):
    """
    Custom permission to allow read-only access to any user.
    """

    def has_permission(self, request, view):
        # Allow access only for safe HTTP methods (GET, HEAD, OPTIONS)
        return request.method in SAFE_METHODS


# @api_view(['GET'])
# @permission_classes([IsAdminOrSuperAdmin])
# def get_user_details(request, user_id):
#     # Code to fetch and return user details
# @permission_classes([IsAdminOrSuperAdmin | ReadOnly])