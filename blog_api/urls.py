from django.urls import path
from django.conf import settings
from django.conf.urls import static

from .views import UploadVideo, GetPublicVideoList

urlpatterns = [
    path("api/upload/video/user/<pk>/", UploadVideo.as_view()),
    path("api/videos/public/", GetPublicVideoList.as_view()),
]
