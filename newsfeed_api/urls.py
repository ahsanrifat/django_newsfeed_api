from django.urls import path
from .views import GetCreateUpdateDeleteNewsFeedSetting

urlpatterns = [
    path("<user>/", GetCreateUpdateDeleteNewsFeedSetting.as_view()),
    # path("newsFeed/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
