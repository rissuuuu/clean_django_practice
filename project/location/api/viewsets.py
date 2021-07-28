from rest_framework import viewsets
from location.api.serializers import ProvinceSerializer, DistrictSerializer
from location.models import Province, District


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = []


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = []

