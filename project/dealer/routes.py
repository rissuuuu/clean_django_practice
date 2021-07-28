from django.urls import path
from dealer.api import viewsets


urlpatterns = [
    path(
        "register_dealer/",
        viewsets.CreateDealerViewSet.as_view({"post": "register_dealer"}),
        name="register_dealer",
    ),
]
