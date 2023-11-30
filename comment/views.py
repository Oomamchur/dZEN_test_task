from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from comment.models import MainComment, Comment
from comment.pagination import CommentPagination
from comment.permissions import (
    IsAdminOrCreatorOrReadOnly,
)
from comment.serializers import (
    MainCommentSerializer,
    MainCommentListSerializer,
    MainCommentDetailSerializer,
    CommentSerializer,
)


class MainCommentViewSet(viewsets.ModelViewSet):
    queryset = MainComment.objects.all()
    serializer_class = MainCommentSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        queryset = self.queryset

        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(user__username__icontains=username)

        return queryset

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ("update", "partial_update", "destroy"):
            return [IsAdminOrCreatorOrReadOnly()]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return MainCommentListSerializer
        if self.action == "retrieve":
            return MainCommentDetailSerializer
        if self.action == "add_comment":
            return CommentSerializer

        return MainCommentSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="add_comment",
        permission_classes=(IsAuthenticated,),
    )
    def add_comment(self, request, pk=None):
        """Endpoint for adding comment to specific post"""
        main_comment = self.get_object()
        user = self.request.user
        Comment.objects.create(
            main_comment=main_comment,
            user=user,
            text=request.data["text"],
        )

        return Response(status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
