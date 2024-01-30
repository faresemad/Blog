from django_filters import rest_framework as filters

from apps.blog.models import Post


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            "title": ["icontains"],
            "user__username": ["icontains"],
            "status": ["exact"],
        }
