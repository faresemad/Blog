from django.contrib import admin

from apps.blog.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish", "status"]
    list_filter = ["status", "created_at", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("publish",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_at", "active"]
    list_filter = ["active", "created_at", "updated_at"]
    search_fields = ["user", "comment"]
