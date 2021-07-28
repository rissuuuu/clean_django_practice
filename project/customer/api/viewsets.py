from django.db import transaction
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from user.api.services import create_user
from customer.api.services import (
    register_customer,
    create_commercial_customer,
    create_residential_customer,
)
from customer.models import Customer


class CreateCustomerViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    @action(["POST"], detail=False)
    @transaction.atomic
    def register_customer(self, request):
        req = request.data
        user = create_user(
            first_name=req.get("first_name"),
            last_name=req.get("last_name"),
            email=req.get("email"),
            password=req.get("password"),
            kwargs={'is_customer':True}
        )
        customer = register_customer(
            user=user,
            first_name=user.first_name,
            middle_name=req.get("middlename"),
            last_name=user.last_name,
            gender=req.get("gender"),
            mobile=req.get("mobile"),
            customer_kind=req.get("customer_kind"),
            picture=req.get("picture"),
        )
        if req.get("customer_kind") == "commercial":
            create_commercial_customer(
                proprieter_name=req.get("proprieter_name"), customer=customer
            )
        if req.get("customer_kind") == "residental":
            create_residential_customer(
                customer=customer, residential_type=req.get("residential_type")
            )
        return Response(customer.to_json())


class GetCustomerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @action(["GET"], detail=True)
    def get_customer(self, request):
        customer = Customer.objects.get(user_id=request.user)
        return Response(customer.to_json())
