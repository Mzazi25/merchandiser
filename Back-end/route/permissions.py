from rest_framework.permissions import BasePermission

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_manager)

class IsMerchandiserUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_merchandiser)
        