from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.blog.feeds import LatestPostsFeed
from apps.blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

# API patterns for Admin
urlpatterns = [
    path("", TemplateView.as_view(template_name="not-found.html"), name="not-found"),
    path(settings.ADMIN_URL, admin.site.urls),
]

# API patterns for Authorization
urlpatterns += [
    path(f"{settings.API_PREFIX}auth/", include("djoser.urls.jwt")),
]

# API patterns for Sitemaps
urlpatterns += [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# API patterns for Spectacular
urlpatterns += [
    path(f"{settings.API_PREFIX}schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{settings.API_PREFIX}docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# API patterns for Apps
urlpatterns += [
    path(f"{settings.API_PREFIX}blog/", include("apps.blog.api.urls")),
    path(f"{settings.API_PREFIX}users/", include("apps.users.api.urls")),
    path(f"{settings.API_PREFIX}feed/rss/", LatestPostsFeed(), name="latest-posts-feed"),
    path(f"{settings.API_PREFIX}profile/", include("apps.profiles.api.urls")),
]
