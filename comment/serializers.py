from rest_framework import serializers

from comment.models import MainComment, Comment


class MainCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainComment
        fields = ("id", "text", "image", "home_page")


class MainCommentListSerializer(MainCommentSerializer):
    class Meta:
        model = MainComment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "image",
            "home_page",
            "comments_count",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "image",
        )


class CommentListSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "image",
        )


class MainCommentDetailSerializer(MainCommentSerializer):
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = MainComment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "image",
            "home_page",
            "comments",
        )
