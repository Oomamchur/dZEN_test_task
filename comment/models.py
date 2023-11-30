from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class MainComment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="main_comments",
        on_delete=models.CASCADE,
    )
    home_page = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def comments_count(self):
        return self.comments.count()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.username} at {self.created_at}"


class Comment(models.Model):
    main_comment = models.ForeignKey(
        MainComment, related_name="comments", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.user.username} at {self.created_at}"
