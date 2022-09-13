from rest_framework.permissions import SAFE_METHODS, BasePermission


class AdminOrReadOnly(BasePermission):
    """The ban on editing if the user is not an admin."""

    def has_permission(self, request, view):
        return (
                request.method in SAFE_METHODS
                or (
                        request.user.is_authenticated
                        and request.user.is_admin)
        )

    def has_object_permission(self, request, view, obj):
        return (
                request.method in SAFE_METHODS
                or (
                        request.user.is_authenticated
                        and request.user.is_admin)
        )


class IsUserForSelfPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAdminOrStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_staff or (
                request.user.is_authenticated and
                request.user.is_admin)
                )


class IsAuthorOrModerPermission(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS:
            return (obj.author == request.user
                    or request.user.is_staff or request.user.is_admin)
        return True
