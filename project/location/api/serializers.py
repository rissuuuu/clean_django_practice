from rest_framework import serializers
from location.models import Province, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(source='district_set',many=True,read_only=True)

    class Meta:
        model = Province
        fields = ['name','districts']




