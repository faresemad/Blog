from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# TODO: Create permissions for the following:
# - IsOwnerOrReadOnly


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
        return obj.user == request.user


class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        return obj.user == request.user
