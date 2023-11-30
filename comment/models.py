import os
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


def comment_image_file_path(instance, filename) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.user.username)}-{uuid.uuid4()}{extension}"

    return os.path.join("media/uploads/comments/", filename)


class MainComment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="main_comments",
        on_delete=models.CASCADE,
    )
    home_page = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to=comment_image_file_path)

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
    image = models.ImageField(null=True, upload_to=comment_image_file_path)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.user.username} at {self.created_at}"
