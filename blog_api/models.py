from django.db import models
from auth_api.models import User
from django.utils import timezone

# Create your models here.
class VideoContents(models.Model):
    video_file = models.FileField(upload_to="blog_videos/%y")
    video_title = models.CharField(max_length=100, blank=False)
    video_description = models.TextField(max_length=1500, blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_videos"
    )
    privacy = models.CharField(max_length=50, default="public")
    liked_by = models.ManyToManyField(User, related_name="liked_videos")
    length = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="blog_videos/thumbnails/%y", blank=True, null=True
    )

    def __str__(self):
        return str(self.id) + "_" + self.video_title + "_" + self.owner.email


class BlogPost(models.Model):
    header_image = models.ImageField(
        upload_to="blog_posts/header_image/", blank=True, null=True
    )
    blog_title = models.CharField(max_length=100, blank=False)
    blog_body = models.TextField(max_length=1500, blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_blogs"
    )
    privacy = models.CharField(max_length=50, default="public")
    liked_by = models.ManyToManyField(User, related_name="liked_blogs")
    length = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + "_" + self.video_title + "_" + self.owner.email
