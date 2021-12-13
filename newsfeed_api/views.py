from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import NewsFeedSettingSerializer
from auth_api.models import User
from .models import NewsFeedSetting
from auth_api.custom_permission import IsAdminOrUser

# Create your views here.
def get_unauthorised_response_json():
    return {"success": False, "message": "Unauthorised Content"}


def get_exception_response_json(e):
    return {"success": False, "message": str(e)}


class GetUpdateNewsFeedSetting(RetrieveUpdateDestroyAPIView):
    queryset = NewsFeedSetting.objects.all()
    serializer_class = NewsFeedSettingSerializer
    lookup_field = "user"
    permission_classes = [IsAdminOrUser]

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser or request.user.id == kwargs["user"]:
                user = User.objects.get(id=kwargs["user"])
                obj, created = NewsFeedSetting.objects.get_or_create(user=user)
                serializer = NewsFeedSettingSerializer(obj)
                return_dict = serializer.data
                return_dict["countries"] = obj.get_list_countries()
                return_dict["sources"] = obj.get_list_sources()
                return_dict["keywords"] = obj.get_list_keywords()
                return Response(return_dict)
            else:
                return Response(get_unauthorised_response_json(), 401)
        except Exception as e:
            return Response(get_exception_response_json(e), 400)

    def patch(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser or request.user.id == kwargs["user"]:
                user = User.objects.get(id=kwargs["user"])
                obj, created = NewsFeedSetting.objects.get_or_create(user=user)
                data = request.data
                print(data)
                res = ""
                for key in data:
                    if key == "countries":
                        obj.countries = data[key]
                        obj.save()
                        res = obj.get_list_countries()
                    if key == "sources":
                        obj.sources = data[key]
                        obj.save()
                        res = obj.get_list_sources()
                    if key == "keywords":
                        obj.keywords = data[key]
                        obj.save()
                        res = obj.get_list_keywords()
                serializer = NewsFeedSettingSerializer(obj)
                return_dict = serializer.data
                return_dict["countries"] = obj.get_list_countries()
                return_dict["sources"] = obj.get_list_sources()
                return_dict["keywords"] = obj.get_list_keywords()
                return Response(return_dict)
            else:
                return Response(get_unauthorised_response_json(), 401)
        except Exception as e:
            return Response(get_exception_response_json(e), 400)

    def put(self, request, *args, **kwargs):
        return Response("Not Allowed", 400)

    def delete(self, request, *args, **kwargs):
        return Response("Not Allowed", 400)


class RetrieveUserNewsFeed(RetrieveAPIView):
    queryset = NewsFeedSetting.objects.all()
    serializer_class = NewsFeedSettingSerializer
    lookup_field = "user"
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser or request.user.id == kwargs["user"]:
                user = User.objects.get(id=kwargs["user"])
                obj, created = NewsFeedSetting.objects.get_or_create(user=user)
                country_list = obj.get_list_countries()
                print(country_list)
                return Response({"": country_list})
            else:
                return Response(get_unauthorised_response_json(), 401)
        except Exception as e:
            return Response(get_exception_response_json(e), 400)
