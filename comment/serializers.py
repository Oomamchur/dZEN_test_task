from rest_framework import serializers

from comment.models import MainComment


class MainCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainComment
        fields = ("id", "user", "text", "home_page", "created_at")
