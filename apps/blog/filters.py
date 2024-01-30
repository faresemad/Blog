from django_filters import rest_framework as filters

from apps.blog.models import Post


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            "title": ["icontains"],
            "slug": ["icontains"],
            "user__username": ["icontains"],
            "body": ["icontains"],
            "publish": ["icontains"],
            "created_at": ["icontains"],
            "updated_at": ["icontains"],
            "status": ["exact"],
        }
