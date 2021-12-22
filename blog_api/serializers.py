from rest_framework import serializers
from .models import VideoContents


class VideoContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContents
        # fields=['id','first_name','last_name','email','password']
        fields = "__all__"
        # exclude = ("password",)
