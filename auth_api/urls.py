from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateNewUser, GetUpdateDeleteUser

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/user/create/", CreateNewUser.as_view()),
    path("api/user/<pk>/", GetUpdateDeleteUser.as_view()),
]
