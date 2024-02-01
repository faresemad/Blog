from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.api.views import UserViewSet, activate_account, reset_password_confirm

router = DefaultRouter()

router.register(r"", UserViewSet, basename="users")

urlpatterns = router.urls
urlpatterns += [
    path("activate-account/<str:uid>/<str:token>/", activate_account, name="activate-account"),
    path("password-reset-account/<str:uid>/<str:token>/", reset_password_confirm, name="reset-password"),
]
