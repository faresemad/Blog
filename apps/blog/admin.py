from django.contrib import admin

from apps.blog.models import Comment, Post, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "publish", "status"]
    list_filter = ["status", "created_at", "publish", "user"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("publish",)}
    raw_id_fields = ["user"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_at", "active"]
    list_filter = ["active", "created_at", "updated_at"]
    search_fields = ["user", "comment"]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "created_at", "active"]
    list_filter = ["active", "created_at", "updated_at"]
    search_fields = ["user", "reply"]
