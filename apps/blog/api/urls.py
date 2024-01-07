from rest_framework_nested import routers

from apps.blog.api.views import CommentViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
comment_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
comment_router.register(r"comments", CommentViewSet, basename="post-comments")
urlpatterns = router.urls + comment_router.urls
