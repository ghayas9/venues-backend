from rest_framework.permissions import BasePermission

class IsAdminOrSuperAdmin(BasePermission):
    """
    Custom permission to only allow admin or superadmin users to access.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and has the required role (admin or superadmin)
        print(request.user.role)
        if request.user.is_authenticated:
            return request.user.role in ['admin', 'super_admin']
        return False


class ReadOnly(BasePermission):
    """
    Custom permission for read-only access. Any user can view the data, but only admins can modify it.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:  # Allow read-only methods
            return True
        
        # For other methods (POST, PUT, DELETE), allow only if the user is admin or superadmin
        return request.user.is_authenticated and request.user.role in ['admin', 'super_admin']
