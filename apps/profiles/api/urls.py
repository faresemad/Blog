from rest_framework.routers import DefaultRouter

from apps.profiles.api.views import LikedPostViewSet, SavedPostViewSet

router = DefaultRouter()
router.register(r"liked", LikedPostViewSet, basename="liked")
router.register(r"saved", SavedPostViewSet, basename="saved")
urlpatterns = router.urls
