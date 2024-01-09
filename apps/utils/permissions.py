from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated

# TODO: Create permissions for the following:
# - IsOwnerOrReadOnly
# - IsAdminUserOrIsSelfOrReadOnly


class IsOwnerOrReadOnly(IsAuthenticated):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if isinstance(request.user, AnonymousUser):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsAdminUserOrIsSelfOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or obj == request.user
