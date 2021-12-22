from django.db import models
from auth_api.models import User
from django.utils import timezone

# Create your models here.
class VideoContents(models.Model):
    video_file = models.FileField(upload_to="video/%y")
    video_title = models.CharField(max_length=100, blank=False)
    video_description = models.TextField(max_length=1500, blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    privacy = models.CharField(max_length=50, default="public")
