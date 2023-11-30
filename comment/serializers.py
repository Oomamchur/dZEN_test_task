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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
        )


class CommentListSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "created_at",
            "text",
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
            "home_page",
            "comments",
        )
