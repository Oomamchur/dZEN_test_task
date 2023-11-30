from django.urls import path, include
from rest_framework import routers

from comment.views import MainCommentViewSet

router = routers.DefaultRouter()
router.register("comments", MainCommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "comment"
