from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsBusinessType(BasePermission):
    """
    - List (GET /offers/): allowed for everyone
    - Detail (GET /offers/<id>/): only for authenticated users
    - Write: only for authenticated business users who are the owner
    """
    
    def has_permission(self, request, view):
         # Always allow safe methods
        if request.method in SAFE_METHODS:
            # Check if it's a detail view -> authentication required
            if view.detail:
                return request.user and request.user.is_authenticated
            # Otherwise (list view), allow for everyone
            return True
        
        # For write operations, only allow if user is authenticated and type is 'business'
        return bool(request.user.is_authenticated and getattr(request.user, 'type', None) == 'business')
    
    def has_object_permission(self, request, view, obj):
        # Always allow safe methods
        if request.method in SAFE_METHODS:
            return True
        
         # Write permission only if the user is the owner of the offer
        return obj.user == request.user