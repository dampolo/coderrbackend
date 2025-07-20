from rest_framework.permissions import BasePermission


class IsBusinessType(BasePermission):
    """
    Allows access only to users with type 'business'.
    """

    def has_permission(self, request, view):
        # Make sure the user is authenticated and has a 'type' attribute
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'type', None) == 'business')