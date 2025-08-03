from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):        
    """
    Custom permission to allow only the owner of an object to edit or delete it.
    
    - Safe methods (GET, HEAD, OPTIONS) are always allowed.
    - For unsafe methods (e.g., PUT, PATCH, DELETE), permission is granted
      only if the object's `id` matches the authenticated user's `id`.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for safe methods
        if request.method in SAFE_METHODS:
            return True
        
        # Allow write/delete only if the user is the owner of the object        
        return obj.id == request.user.id