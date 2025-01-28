from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsVenueOwner(BasePermission):
    """
    Custom permission to allow only venue owners to manage their own venues.
    """

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission to check if the requesting user is the owner of the venue.
        """
        return obj.owner == request.user


class IsAdminOrSuperAdmin(BasePermission):
    """
    Custom permission to grant access to both admin and super admin users.
    """

    def has_permission(self, request, view):
        """
        Global-level permission to check if the user is authenticated and is either an admin or super admin.
        """
        return request.user.is_authenticated and request.user.role in ['admin', 'super_admin']


class ReadOnly(BasePermission):
    """
    Custom permission to allow read-only access for unauthenticated or authenticated users.
    """

    def has_permission(self, request, view):
        """
        Allow access only for safe HTTP methods (GET, HEAD, OPTIONS).
        """
        return request.method in SAFE_METHODS


class IsSuperAdmin(BasePermission):
    """
    Custom permission to grant access only to super admin users.
    """

    def has_permission(self, request, view):
        """
        Check if the requesting user is a super admin.
        """
        return request.user.is_authenticated and request.user.role == 'super_admin'
