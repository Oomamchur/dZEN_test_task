from rest_framework import serializers

from comment.models import MainComment, Comment


class MainCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainComment
        fields = ("id", "text", "home_page")


class MainCommentListSerializer(MainCommentSerializer):
    class Meta:
        model = MainComment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "home_page",
            "comments_count",
        )


class MainCommentDetailSerializer(MainCommentSerializer):
    class Meta:
        model = MainComment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "home_page",
            "comments",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
        )
