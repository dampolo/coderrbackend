from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrderAccessAllowed(BasePermission):
    """
    Permission class that controls access to Order objects.

    - Only users with type 'customer' can create orders (POST).
    - Only users with type 'business' can update orders (PUT/PATCH),
      and only if they are the assigned business_user of the order.
    - All other methods (e.g., GET, DELETE) are allowed by default.
    """

    def has_permission(self, request, view):
        user = request.user
        user_type = getattr(user, 'type', None)

        # Block unauthenticated users entirely
        if not user or not user.is_authenticated:
            return False

        if request.method == 'POST':
            # Only customers can create an order
            return user_type == 'customer'

        if request.method in ['PUT', 'PATCH']:
            # Only business users can update orders
            return user_type == 'business'
        
        if request.method == 'DELETE':
            return user.is_staff

        # Allow GET and other safe methods to any authenticated user
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

         # Only business users can modify their own orders
        if request.method in ['PUT', 'PATCH']:
            return (
                getattr(request.user, 'type', None) == 'business' and 
                obj.business_user == request.user
            )

        return True