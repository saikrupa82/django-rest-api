from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.is_admin:
            return True
        else:
            return False


class IsNotAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.role.is_admin:
            return True
        else:
            return False
