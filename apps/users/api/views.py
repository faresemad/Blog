from django.conf import settings
from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(DjoserUserViewSet):
    # def create(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return Response({"detail": "User registration is disabled."}, status=status.HTTP_403_FORBIDDEN)
    #     else:
    #         return super().create(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return Response({"status": "user created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(response.data, status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "user deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=response.status_code)

    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        try:
            response = super().activation(request, *args, **kwargs)
        except exceptions.PermissionDenied as e:  # noqa
            return render(request, "users/already_activated.html")

        if response.status_code == 204:
            return render(request, "users/activation_success.html")
        else:
            return render(request, "users/activation_failed.html")

    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        response = super().resend_activation(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "activation email sent"}, status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response({"status": "user already activated"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(response.data, status=response.status_code)

    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        response = super().set_password(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "password changed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=response.status_code)

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        response = super().reset_password(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "password reset email sent"}, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=response.status_code)

    @action(["post"], detail=False)
    def reset_password_confirm(self, request, *args, **kwargs):
        try:
            response = super().reset_password_confirm(request, *args, **kwargs)
        except exceptions.ValidationError as e:  # noqa
            return render(request, "users/reset_password_confirm.html")
        if response.status_code == 204:
            return render(request, "users/password_changed.html")
        else:
            return Response(response.data, status=response.status_code)


def activate_account(request, uid, token):
    PROTOCOL = getattr(settings, "PROTOCOL") or "https"
    DOMAIN = getattr(settings, "DOMAIN") or "server.django-blog.com"
    ACTIVATE_ACCOUNT_URL = getattr(settings, "ACTIVATE_ACCOUNT_URL") or "users/activation/"
    return render(
        request,
        "users/activate_account.html",
        {
            "uid": uid,
            "token": token,
            "activate_account_url": f"{PROTOCOL}://{DOMAIN}/{settings.API_PREFIX}{ACTIVATE_ACCOUNT_URL}",
        },
    )


def reset_password_confirm(request, uid, token):
    PROTOCOL = getattr(settings, "PROTOCOL") or "https"
    DOMAIN = getattr(settings, "DOMAIN") or "server.django-blog.com"
    RESET_PASS_CONFIRM_URL = getattr(settings, "RESET_PASS_CONFIRM_URL") or "users/reset_password_confirm/"
    return render(
        request,
        "users/reset_password_confirm.html",
        {
            "uid": uid,
            "token": token,
            "reset_pass_confirm_url": f"{PROTOCOL}://{DOMAIN}/{settings.API_PREFIX}{RESET_PASS_CONFIRM_URL}",
        },
    )
