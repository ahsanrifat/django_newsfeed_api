from django.db.models import fields
from rest_framework import serializers
from .models import NewsFeedSetting


class NewsFeedSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFeedSetting
        fields = "__all__"
