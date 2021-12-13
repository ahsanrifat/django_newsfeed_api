from django.db import models
from auth_api.models import User
import json

# Create your models here.
class NewsFeedSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    countries = models.CharField(max_length=900, blank=True)
    sources = models.CharField(max_length=900, blank=True)
    keywords = models.CharField(max_length=1000, blank=True)

    class Meta:
        db_table = "custom_user_news_settings"

    def __str__(self):
        return self.email

    def split_str(self, s):
        if s == "":
            return []
        return s.split(",")

    def get_list_countries(self):
        return self.split_str(self.countries)

    def get_list_sources(self):
        return self.split_str(self.sources)

    def get_list_keywords(self):
        return self.split_str(self.keywords)
