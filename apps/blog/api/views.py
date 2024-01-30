from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
from apps.blog.filters import PostFilter
from apps.blog.models import Comment, Post, Reply
from apps.utils.paginations import PostPagination
from apps.utils.permissions import IsOwnerOrReadOnly
from apps.utils.tasks import check_depug


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    http_method_names = ["get", "post", "patch", "delete"]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        elif self.action == "destroy":
            return PostDeleteSerializer
        elif self.action == "retrieve":
            return PostRetrieveSerializer
        return PostListSerializer

    def list(self, queryset, *args, **kwargs):
        check_depug.delay()
        return super().list(queryset, *args, **kwargs)

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = []
        elif self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentListSerializer
    http_method_names = ["get", "post", "patch", "delete"]
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

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = []
        elif self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

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
    http_method_names = ["get", "post", "patch", "delete"]
    lookup_field = "id"

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

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = []
        elif self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
