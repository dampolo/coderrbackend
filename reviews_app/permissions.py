from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReviewerOrReadOnly(BasePermission):
    """
    Allows read access to anyone authenticated,
    but write access only to the reviewer who created the review.
    """

    def has_permission(self, request, view):
        # Allow all authenticated users to view or create
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # Allow GET, HEAD, OPTIONS
        return obj.reviewer == request.user  # Only reviewer can modify