from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from location.api.serializers import ProvinceSerializer, DistrictSerializer
from location.models import Province, District


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
