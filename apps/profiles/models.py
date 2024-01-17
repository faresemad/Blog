from django.contrib.auth import get_user_model
from django.db import models

from apps.blog.models import Post

User = get_user_model()


class LikedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.post}"

    class Meta:
        verbose_name = "Like Post"
        verbose_name_plural = "Likes Post"
        unique_together = ("user", "post")

    def save(self, *args, **kwargs):
        if self.user == self.post.user:
            raise ValueError("You cannot like your own post")
        super().save(*args, **kwargs)


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.post}"

    class Meta:
        verbose_name = "Saved Post"
        verbose_name_plural = "Saved Posts"
        unique_together = ("user", "post")

    def save(self, *args, **kwargs):
        if self.user == self.post.user:
            raise ValueError("You cannot save your own post")
        super().save(*args, **kwargs)
