from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class MainComment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="main_comments",
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=255)
    home_page = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    main_comment = models.ForeignKey(
        MainComment, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=255)
    home_page = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
