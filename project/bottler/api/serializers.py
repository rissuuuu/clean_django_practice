from django.shortcuts import get_object_or_404
from rest_framework import serializers
from bottler.models import Bottler, Brand, UserBrand, DealerBrand


class BottlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottler
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class UserBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBrand
        fields = "__all__"
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        request = self.context["request"]
        obj = UserBrand.objects.filter(
            user_id=request.user, brand_id=validated_data.get("brand_id")
        ).exists()
        if not obj:
            return UserBrand.objects.create(user_id=request.user, **validated_data)
        else:
            raise serializers.ValidationError("User brand already exist")


class DealerBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerBrand
        fields = "__all__"
        read_only_fields = ["dealer_id"]

    def create(self, validated_data):
        request = self.context["request"]
        obj = DealerBrand.objects.filter(
            dealer_id=request.user.dealer, brand_id=validated_data.get("brand_id")
        ).exists()
        if not obj:
            return DealerBrand.objects.create(
                dealer_id=request.user.dealer, **validated_data
            )
        else:
            raise serializers.ValidationError("Dealer brand already exist")
