from rest_framework.response import Response
from rest_framework import viewsets
from django.db import transaction
from rest_framework.decorators import action
from user.api.services import create_user
from dealer.api.services import create_dealer


class CreateDealerViewSet(viewsets.ViewSet):
    @transaction.atomic
    @action(["POST"], detail=True)
    def register_dealer(self, request):
        req = request.data
        user = create_user(
            first_name=req.get("first_name"),
            last_name=req.get("last_name"),
            email=req.get("email"),
            password=req.get("password"),
            kwargs={"is_dealer": True},
        )
        dealer = create_dealer(
            first_name=req.get("first_name"),
            middle_name=req.get("middle_name"),
            last_name=req.get("last_name"),
            province=req.get("province"),
            district=req.get("district"),
            latitude=req.get("latitude"),
            longitude=req.get("longitude"),
            mobile=req.get("mobile"),
            email=req.get("email"),
            user_id=user,
        )
        return Response(dealer.to_json())
