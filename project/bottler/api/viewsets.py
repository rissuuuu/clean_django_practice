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
from project.permissions.permissions import AllowAdmin


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
            return super(BottlerViewSet, self).get_permissions()
        if self.action == "create" or self.action == "update":
            return [AllowAdmin()]


class UserBrandViewSet(viewsets.ModelViewSet):
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


class DealerBrandViewSet(viewsets.ModelViewSet):
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
