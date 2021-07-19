from django.conf.urls import url
from user.api.viewsets import NOCTokenObtainPairView

urlpatterns = [
    url(r'^api/v1/auth/jwt/create/',
            NOCTokenObtainPairView.as_view(),
            name='token_obtain_pair'
            ),
]