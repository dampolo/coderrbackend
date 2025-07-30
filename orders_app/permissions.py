from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrderAccessAllowed(BasePermission):
    """
    Allows access only to users with type 'customer'.
    """

    def has_permission(self, request, view):
        user = request.user
        user_type = getattr(user, 'type', None)

        if not user.is_authenticated:
            return False

        if request.method == 'POST':
            # Nur customer dürfen Bestellungen erstellen
            return user_type == 'customer'

        if request.method in ['PUT', 'PATCH']:
            # Nur business user dürfen bearbeiten (Objektprüfung erfolgt später)
            return user_type == 'business'

        # Alle anderen Methoden wie GET, DELETE usw.
        return True  # oder False, wenn du das einschränken willst
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Nur business user darf seine eigene Bestellung bearbeiten
        if request.method in ['PUT', 'PATCH']:
            return (
                getattr(request.user, 'type', None) == 'business' and 
                obj.business_user == request.user
            )

        return True