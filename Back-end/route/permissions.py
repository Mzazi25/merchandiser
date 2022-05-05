<<<<<<< HEAD
from rest_framework.permissions import BasePermission

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_manager)

class IsMerchandiserUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_merchandiser)
        
=======
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
>>>>>>> e3ae484b90ce5a45f22fa70400e16fa3bee94612
