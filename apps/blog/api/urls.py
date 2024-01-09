from rest_framework_nested import routers

from apps.blog.api.views import CommentViewSet, PostViewSet, ReplyViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)

comment_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
comment_router.register(r"comments", CommentViewSet, basename="post-comments")

reply_router = routers.NestedSimpleRouter(comment_router, r"comments", lookup="comment")
reply_router.register(r"replies", ReplyViewSet, basename="comment-replies")

urlpatterns = router.urls + comment_router.urls + reply_router.urls
