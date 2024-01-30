from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.profiles.api.serializers import (
    LikedPostListSerializer,
    LikedPostSerializer,
    SavedPostListSerializer,
    SavedPostSerializer,
)
from apps.profiles.models import LikedPost, SavedPost
from apps.utils.permissions import IsOwner


class LikedPostViewSet(viewsets.ModelViewSet):
    serializer_class = LikedPostSerializer
    queryset = LikedPost.objects.all()
    permission_classes = [IsOwner]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return LikedPostListSerializer
        return LikedPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class SavedPostViewSet(viewsets.ModelViewSet):
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()
    permission_classes = [IsOwner]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return SavedPostListSerializer
        return SavedPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
