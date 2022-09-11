from rest_framework.permissions import SAFE_METHODS, BasePermission

class AdminOrReadOnly(BasePermission):
    """The ban on editing if the user is not an admin."""

    def has_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS or (request.user.is_authenticated
                and request.user.is_admin))
