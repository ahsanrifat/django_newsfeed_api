from django.shortcuts import render
from .models import VideoContents
from auth_api.custom_permission import IsAdminOrUser
from auth_api.models import User
from auth_api.views import get_exception_response_json
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import VideoContentsSerializer
import time
from .helper_functions import (
    PIL_image_to_django_file,
    generate_thumbnail_from_video_file,
)

from django.conf import settings
from moviepy.editor import *
import ipdb

# Create your views here.
class GetPublicVideoList(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = VideoContentsSerializer

    def get_queryset(self):
        return VideoContents.objects.filter(privacy="public")

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response(get_exception_response_json(e), 400)


class UploadVideo(CreateAPIView):
    queryset = VideoContents.objects.all()
    # serializer_class = UserCreateSerializer
    permission_classes = [IsAdminOrUser]

    def post(self, request, *args, **kwargs):
        try:
            user_obj = User.objects.get(id=kwargs.get("pk"))
            video_file = request.data["video"]
            if video_file.name.split(".")[-1] in ("avi", "mp4", "mkv"):
                video_name = (
                    str(kwargs.get("pk")) + "_" + str(time.time()) + "_video_file"
                )
                video_file.name = video_name + "." + video_file.name.split(".")[-1]
                video_obj = VideoContents(
                    video_file=video_file,
                    video_title=request.data["video_title"],
                    owner=user_obj,
                )

                video_obj.save()
                video_file_path = (
                    rf"{settings.MEDIA_ROOT}\blog_videos\21\{video_file.name}"
                )
                vid_movie_py = VideoFileClip(rf"{video_file_path}")
                img = generate_thumbnail_from_video_file(vid_movie_py)
                video_obj.thumbnail = PIL_image_to_django_file(img, video_name)
                video_obj.length = vid_movie_py.duration / 60
                video_obj.save()
                return Response(
                    {
                        "success": True,
                        "message": "Video Uploaded Successfully",
                        "video_file_path": video_obj.video_file.url,
                        "video_duration": video_obj.length,
                        "thumbnail_url": video_obj.thumbnail.url,
                    }
                )
            else:
                return Response(
                    {
                        "success": False,
                        "message": "Invalid file format",
                        "accepted_formats": "avi, mp4, mkv",
                        "given_format": video_file.name.split(".")[-1],
                    }
                )
        except Exception as e:
            return Response(get_exception_response_json(e), 400)
