from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj: Post):
        return obj.updated_at

    def location(self, obj):
        return reverse("post-detail", args=[obj.slug])
