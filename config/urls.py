from django.contrib import admin
from django.urls import include, path

api_prefix = "api/"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(f"{api_prefix}blog/", include("apps.blog.api.urls")),
    path(f"{api_prefix}profile/", include("apps.profiles.api.urls")),
]
