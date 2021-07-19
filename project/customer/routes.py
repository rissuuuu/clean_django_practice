from django.urls import path
from customer.api import viewsets
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path(
        "register_customer/",
        viewsets.CustomerViewSet.as_view({"post": "register_customer"}),
        name="register_customer",
    ),
    path(
        "current_customer/",
        viewsets.CustomerViewSet.as_view({"get": "get_customer"}),
        name="get_customer",
    ),
    url(r"^auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
