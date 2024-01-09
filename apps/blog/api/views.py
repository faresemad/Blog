from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.blog.api.serializers import (
    CommentCreateSerializer,
    CommentDeleteSerializer,
    CommentListSerializer,
    CommentRetrieveSerializer,
    CommentUpdateSerializer,
    PostCreateSerializer,
    PostDeleteSerializer,
    PostListSerializer,
    PostRetrieveSerializer,
    ReplyCreateSerializer,
    ReplyDeleteSerializer,
    ReplyListSerializer,
    ReplyRetrieveSerializer,
    ReplyUpdateSerializer,
)
from apps.blog.models import Comment, Post, Reply


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        elif self.action == "destroy":
            return PostDeleteSerializer
        elif self.action == "retrieve":
            return PostRetrieveSerializer
        return PostListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentListSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Comment.objects.filter(post__slug=self.kwargs.get("post_slug"))

    def get_serializer_class(self):
        if self.action == "create":
            return CommentCreateSerializer
        elif self.action == "destroy":
            return CommentDeleteSerializer
        elif self.action == "retrieve":
            return CommentRetrieveSerializer
        elif self.action == "update" or self.action == "partial_update":
            return CommentUpdateSerializer
        return CommentListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplyListSerializer
    lookup_field = "id"
    # allowed_methods = ["GET", "POST", "PATCH", "DELETE"]

    def get_queryset(self):
        return Reply.objects.filter(comment_id=self.kwargs.get("comment_id"))

    def get_serializer_class(self):
        if self.action == "create":
            return ReplyCreateSerializer
        elif self.action == "destroy":
            return ReplyDeleteSerializer
        elif self.action == "retrieve":
            return ReplyRetrieveSerializer
        elif self.action == "update" or self.action == "partial_update":
            return ReplyUpdateSerializer
        return ReplyListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
