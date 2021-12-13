from django.urls import path
from .views import GetUpdateNewsFeedSetting, RetrieveUserNewsFeed

urlpatterns = [
    path("user/setting/<user>/", GetUpdateNewsFeedSetting.as_view()),
    path("user/news/<user>/", RetrieveUserNewsFeed.as_view()),
    # path("newsFeed/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
