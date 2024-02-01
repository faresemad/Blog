from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone")
    search_fields = ("username", "email", "phone")
    ordering = ("username",)
