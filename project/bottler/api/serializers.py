from rest_framework import serializers
from bottler.models import Bottler, Brand, UserBrand, DealerBrand


class BottlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottler
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UserBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBrand
        fields = '__all__'


class DealerBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerBrand
        fields = '__all__'
