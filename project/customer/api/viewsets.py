import logging
from django.db import transaction
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from customer.api.services import create_user, register_customer


class CreateCustomerViewSet(viewsets.ViewSet):
    @action(["POST"], detail=False)
    @transaction.atomic
    def register_customer(self, request):
        req = request.data
        user = create_user(
            first_name=req.get("first_name"),
            last_name=req.get("last_name"),
            username=req.get("username"),
            email=req.get("email"),
            password=req.get("password"),
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
        # return Response(customer.to_json())
        if req.get("customer_kind") == "commercial":
            create_commercial_customer(
                proprieter_name = req.get("proprieter_name"),
                customer_id = req.get("customer_id")
            )
        if req.get("customer_kind") == "residental":
            create_residential_customer(
                customer_id = customer,
                kind = req.get("residential_type")
            )





