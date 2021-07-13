from django.urls import path
from customer.api import viewsets

urlpatterns = [
    path(
        "register_customer/",
        viewsets.CreateCustomerViewSet.as_view({"post": "register_customer"}),
        name="register_customer",
    ),
]
