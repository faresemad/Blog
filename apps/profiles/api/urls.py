from rest_framework.routers import DefaultRouter

from apps.profiles.api.views import ArchivedPostsViewSet, DRAFTPostsViewSet, LikedPostViewSet, SavedPostViewSet

router = DefaultRouter()
router.register(r"liked", LikedPostViewSet, basename="liked")
router.register(r"saved", SavedPostViewSet, basename="saved")
router.register(r"archived", ArchivedPostsViewSet, basename="archived")
router.register(r"draft", DRAFTPostsViewSet, basename="draft")

urlpatterns = router.urls
