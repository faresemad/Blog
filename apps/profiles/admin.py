from django.contrib import admin

from apps.profiles.models import LikedPost, SavedPost

admin.site.register(LikedPost)
admin.site.register(SavedPost)
