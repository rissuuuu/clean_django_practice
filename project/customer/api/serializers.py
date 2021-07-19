from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class NOCTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except Exception:
            try:
                user = get_user_model().objects.get(email=attrs["email"])
                check_password = user.check_password(attrs["password"])
                if user.is_active:
                    data = super().validate(attrs)
                elif check_password:
                    data = {
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    }
                else:
                    data = super().validate(attrs)
            except ObjectDoesNotExist:
                data = super().validate(attrs)
        return {"data": {"token": data}, "message": "Success", "error": ""}

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
