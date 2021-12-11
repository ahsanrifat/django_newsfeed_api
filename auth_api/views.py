from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import UserCreateSerializer

# from django.core.exceptions import PermissionDenied
from .models import User

# Create your views here.


def get_unauthorised_response_json():
    return {"success": False, "message": "Unauthorised Content"}


def get_exception_response_json(e):
    return {"success": False, "message": str(e)}


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
            return Response(get_exception_response_json(e), 400)


class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        #
        try:
            # if it's a admin's token
            if request.user.is_superuser:
                response = super().delete(request, *args, **kwargs)
                if response.status_code == 204:
                    return Response({"success": True, "message": "Deleted User"})
                return response
            else:
                return Response(
                    {"success": False, "message": "Only an Admin can delete an user"},
                    401,
                )
        except Exception as e:
            print("Exception in delete user-->", e)
            return Response(get_exception_response_json(e), 400)

    def patch(self, request, *args, **kwargs):
        try:
            # password changing mechanism
            if "password" in request.data:
                instance = self.get_object()
                instance.set_password(request.data["password"])
                return Response(
                    {"success": True, "message": "Password Changed Successfully"}
                )
            elif "password" not in request.data:
                response = super().patch(request, *args, **kwargs)
                return Response({"success": True, "message": "Data updated partially"})
        except Exception as e:
            print("Exception in patch user-->", e)
            return Response(get_exception_response_json(e), 400)

    def put(self, request, *args, **kwargs):
        return Response({"success": False, "message": "PUT not allowed"}, 400)
