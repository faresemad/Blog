from rest_framework import serializers

from apps.blog.api.serializers import PostListSerializer
from apps.profiles.models import LikedPost, SavedPost


class LikedPostListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = PostListSerializer(read_only=True)

    class Meta:
        model = LikedPost
        fields = "__all__"


class LikedPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LikedPost
        fields = "__all__"


class SavedPostListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = PostListSerializer(read_only=True)

    class Meta:
        model = SavedPost
        fields = "__all__"


class SavedPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SavedPost
        fields = "__all__"
