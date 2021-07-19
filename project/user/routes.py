from django.conf.urls import url
from user.api.viewsets import NOCTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    url("auth/jwt/create/", NOCTokenObtainPairView.as_view(), name="token_obtain_pair"),
    url("auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
