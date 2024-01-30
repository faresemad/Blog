from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.blog.feeds import LatestPostsFeed
from apps.blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}


api_prefix = "api/"
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(f"{api_prefix}auth/", include("djoser.urls")),
    path(f"{api_prefix}auth/", include("djoser.urls.jwt")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# API patterns
urlpatterns += [
    path(f"{api_prefix}blog/", include("apps.blog.api.urls")),
    path(f"{api_prefix}feed/rss/", LatestPostsFeed(), name="latest-posts-feed"),
    path(f"{api_prefix}profile/", include("apps.profiles.api.urls")),
]
