from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReviewerOrReadOnly(BasePermission):
    """
    Custom permission:
    - Authenticated users can read any review (GET, HEAD, OPTIONS).
    - Only 'customer' users can create, update, or delete reviews.
    - Only the original reviewer can update or delete their own review.
    """

    def has_permission(self, request, view):
        user = request.user

        # Must be authenticated for any method
        if not user or not user.is_authenticated:
            return False

        user_type = getattr(user, 'type', None)

        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # Only users with type 'customer' can create or modify reviews
            return user_type == 'customer'

        # For safe methods like GET, allow all authenticated users
        return True
    
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to all authenticated users
        if request.method in SAFE_METHODS:
            # Only the original reviewer (with type 'customer') can modify/delete
            return True
        return obj.reviewer == request.user and getattr(request.user, 'type', None) == 'customer'  # Only reviewer can modify