from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import NewsFeedSettingSerializer
from auth_api.models import User
from .models import NewsFeedSetting

# Create your views here.
def get_unauthorised_response_json():
    return {"success": False, "message": "Unauthorised Content"}


def get_exception_response_json(e):
    return {"success": False, "message": str(e)}


class GetCreateUpdateDeleteNewsFeedSetting(RetrieveUpdateDestroyAPIView):
    queryset = NewsFeedSetting.objects.all()
    serializer_class = NewsFeedSettingSerializer
    lookup_field = "user"
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser or request.user.id == kwargs["user"]:
                user = User.objects.get(id=kwargs["user"])
                obj, created = NewsFeedSetting.objects.get_or_create(user=user)
                serializer = NewsFeedSettingSerializer(obj)
                return Response(serializer.data)
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
                        obj.set_list_countries(data[key])
                        obj.save()
                        res = obj.get_list_countries()
                        print(res)
                    if key == "sources":
                        obj.set_list_sources(data[key])
                        obj.save()
                        res = obj.get_list_sources()
                        print(res)
                    if key == "keywords":
                        obj.set_list_keywords(data[key])
                        obj.save()
                        res = obj.get_list_keywords()
                        print(res)
                serializer = NewsFeedSettingSerializer(obj)
                return Response(serializer.data)
            else:
                return Response(get_unauthorised_response_json(), 401)
        except Exception as e:
            return Response(get_exception_response_json(e), 400)
