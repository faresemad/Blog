from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed

from apps.blog.models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = "application/xml"

    def rss_attributes(self):
        attrs = super().rss_attributes()
        attrs["version"] = "2.0"
        return attrs


class LatestPostsFeed(Feed):
    feed_type = ExtendedRSSFeed
    title = "Your Blog Title"
    link = "/"
    description = "Latest posts from Your Blog"

    def items(self):
        return Post.objects.all()[:10]

    def item_title(self, item: Post):
        return item.title

    def item_description(self, item: Post):
        return item.body

    def item_link(self, item: Post):
        return reverse("post-detail", args=[item.slug])
