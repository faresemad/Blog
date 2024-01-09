from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.timesince import timesince
from rest_framework import serializers

from apps.blog.models import Comment, Post, Reply

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
        ]

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


class ReplyCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reply
        fields = [
            "user",
            "reply",
        ]

    def create(self, *args, **kwargs):
        comment_id = self.context["view"].kwargs.get("comment_id")
        comment = Comment.objects.get(id=comment_id)
        reply = Reply.objects.create(comment=comment, **self.validated_data)
        return reply


class ReplyDeleteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
        ]

    def validate(self, attrs):
        reply_id = attrs.get("id")
        try:
            reply = Reply.objects.get(id=reply_id)
        except Reply.DoesNotExist:
            raise serializers.ValidationError("Reply does not exist")
        if reply.user != self.context["request"].user:
            raise serializers.ValidationError("You are not the author of this reply")
        return attrs


class ReplyRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
            "reply",
        ]


class ReplyUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
            "reply",
        ]


class ReplyListSerializer(serializers.ModelSerializer):
    time_stamp = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
            "time_stamp",
            "reply",
        ]

    def get_time_stamp(self, obj):
        publish_date = obj.created_at
        todat = timezone.now()
        time_delta = timesince(publish_date, todat)
        return time_delta


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            "comment",
            "user",
        ]

    def create(self, *args, **kwargs):
        post_slug = self.context["view"].kwargs.get("post_slug")
        post = Post.published.get(slug=post_slug)
        comment = Comment.objects.create(post=post, **self.validated_data)
        return comment


class CommentDeleteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
        ]

    def validate(self, attrs):
        comment_id = attrs.get("id")
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise serializers.ValidationError("Comment does not exist")
        if comment.user != self.context["request"].user:
            raise serializers.ValidationError("You are not the author of this comment")
        return attrs


class CommentRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    replies_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "comment",
            "replies_comment",
        ]

    def get_replies_comment(self, obj):
        replies = obj.replies_comment.all()
        return ReplyListSerializer(replies, many=True).data


class CommentListSerializer(serializers.ModelSerializer):
    time_stamp = serializers.SerializerMethodField()
    user = UserSerializer()
    replies_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "time_stamp",
            "user",
            "replies_comment",
        ]

    def get_time_stamp(self, obj):
        publish_date = obj.created_at
        todat = timezone.now()
        time_delta = timesince(publish_date, todat)
        return time_delta

    def get_replies_comment(self, obj):
        replies = obj.replies_comment.all()
        return ReplyListSerializer(replies, many=True).data


class CommentUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "user",
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "author",
            "publish",
            "status",
            "tags",
        ]


class PostListSerializer(serializers.ModelSerializer):
    time_stamp = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            "time_stamp",
            "author",
            "body",
            "status",
            "tags",
        ]

    def get_time_stamp(self, obj):
        publish_date = obj.publish
        todat = timezone.now()
        time_delta = timesince(publish_date, todat)
        return time_delta


class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
        ]

    def validate(self, attrs):
        post_id = attrs.get("id")
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post does not exist")
        if post.author != self.context["request"].user:
            raise serializers.ValidationError("You are not the author of this post")
        return attrs


class PostRetrieveSerializer(serializers.ModelSerializer):
    time_stamp = serializers.SerializerMethodField()
    comments_post = CommentListSerializer(many=True, read_only=True)
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            "publish",
            "time_stamp",
            "author",
            "body",
            "status",
            "tags",
            "comments_post",
        ]

    def get_time_stamp(self, obj):
        publish_date = obj.publish
        todat = timezone.now()
        time_delta = timesince(publish_date, todat)
        return time_delta
