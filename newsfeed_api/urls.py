from django.urls import path
from .views import GetUpdateNewsFeedSetting

urlpatterns = [
    path("<user>/", GetUpdateNewsFeedSetting.as_view()),
    # path("newsFeed/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
