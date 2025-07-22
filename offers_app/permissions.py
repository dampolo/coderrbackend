from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBusinessType(BasePermission):
    """
    Allows safe (read-only) access to everyone, but write access only to 'business' users.
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in SAFE_METHODS:
            return True
        # For write operations, only allow if user is authenticated and type is 'business'
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'type', None) == 'business')