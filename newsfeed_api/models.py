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

    def set_list_countries(self, list_obj):
        self.countries = json.dumps(list_obj)

    def get_list_countries(self):
        return json.loads(self.countries)

    def set_list_sources(self, list_obj):
        self.sources = json.dumps(list_obj)

    def get_list_sources(self):
        return json.loads(self.sources)

    def set_list_keywords(self, list_obj):
        self.keywords = json.dumps(list_obj)

    def get_list_keywords(self):
        return json.loads(self.keywords)
