from rest_framework_simplejwt.views import TokenObtainPairView


from user.api.serializers import NOCTokenObtainPairSerializer


class NOCTokenObtainPairView(TokenObtainPairView):
    serializer_class = NOCTokenObtainPairSerializer
