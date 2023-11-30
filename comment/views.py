from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from comment.models import MainComment
from comment.serializers import MainCommentSerializer


class MainCommentViewSet(viewsets.ModelViewSet):
    queryset = MainComment.objects.all()
    serializer_class = MainCommentSerializer
    permission_classes = (AllowAny,)
