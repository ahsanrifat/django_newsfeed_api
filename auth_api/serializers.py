from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework.response import Response


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields=['id','first_name','last_name','email','password']
        fields = "__all__"
        # exclude = ("password",)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        if password is not None:
            if len(password) > 4:
                instance = self.Meta.model(**validated_data)
                instance.set_password(password)
                instance.save()
                return instance
        raise serializers.ValidationError("Password requirements did not match")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data["refresh"] = str(refresh)
            data.pop("refresh", None)  # remove refresh from the payload
            data["access"] = str(refresh.access_token)

            # Add extra responses here
            data["user_id"] = self.user.id
            data["email"] = self.user.email
            data["full_name"] = self.user.full_name
            data["is_admin"] = self.user.is_superuser
            data["is_stuff"] = self.user.is_staff
            # data["date"] = datetime.date.today()
            return data
        except Exception as e:
            return {"success": False, "message": str(e)}
