from rest_framework import permissions


class ReadOnlyOrIsAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     return request.user and request.user.is_staff

class IsLogged(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated