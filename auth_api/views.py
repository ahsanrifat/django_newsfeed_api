from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserCreateSerializer
from django.core.exceptions import PermissionDenied
from .models import User

# Create your views here.
class CreateNewUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            if response.status_code == 201:
                return Response(
                    {"success": True, "Message": "User Created Successfully"}
                )
            else:
                return Response({"success": False, "Message": response.message})
        except Exception as e:
            return Response({"success": False, "Message": e.get_full_details()})


class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        # return super().delete(request, *args, **kwargs)
        try:
            # if it's a admin's token
            if request.user.is_superuser:
                return Response(
                    {"success": True, "user": "admin", "message": "Deleted"}
                )
            else:
                return Response(
                    {"success": False, "message": "Only an Admin can delete an user"}
                )
        except Exception as e:
            return Response({"success": False, "message": "Exception"})
