from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from bottler.api.serializers import (
    BottlerSerializer,
    BrandSerializer,
    DealerBrandSerializer,
    UserBrandSerializer,
)
from bottler.models import Bottler, Brand, UserBrand, DealerBrand
from project.permissions.permissions import AllowAdmin, AllowDealer, AllowCustomer


class BottlerViewSet(viewsets.ModelViewSet):
    queryset = Bottler.objects.all()
    serializer_class = BottlerSerializer
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            return super(BottlerViewSet, self).get_permissions()
        if self.action == "create" or self.action == "update":
            return [AllowAdmin()]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            return super(BrandViewSet, self).get_permissions()
        if self.action == "create" or self.action == "update":
            return [AllowAdmin()]


class UserBrandViewSet(viewsets.ModelViewSet):
    queryset = UserBrand.objects.all()
    serializer_class = UserBrandSerializer
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            return super(UserBrandViewSet, self).get_permissions()
        if self.action == "create" or self.action == "update":
            return [AllowCustomer()]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserBrand.objects.all()
        elif self.request.user.is_customer:
            return UserBrand.objects.filter(user_id=self.request.user)


class DealerBrandViewSet(viewsets.ModelViewSet):
    queryset = DealerBrand.objects.all()
    serializer_class = DealerBrandSerializer
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            return super(DealerBrandViewSet, self).get_permissions()
        if self.action == "create" or self.action == "update":
            return [AllowDealer()]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return DealerBrand.objects.all()
        elif self.request.user.is_dealer:
            return DealerBrand.objects.filter(dealer_id=self.request.user.dealer)
