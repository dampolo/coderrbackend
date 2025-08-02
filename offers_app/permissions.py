from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsBusinessType(BasePermission):
    """
    Allows safe (read-only) access to anyone.
    Write access is only allowed to authenticated 'business' users
    who are the owner of the offer.
    """
    def has_permission(self, request, view):
        # For write operations, only allow if user is authenticated and type is 'business'
        return bool(request.user.is_authenticated and getattr(request.user, 'type', None) == 'business')
    
    def has_object_permission(self, request, view, obj):
        # Always allow safe methods
        if request.method in SAFE_METHODS:
            return True
        
         # Write permission only if the user is the owner of the offer
        return obj.user == request.user