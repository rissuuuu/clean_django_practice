from django.db import models
from user.models import User
from dealer.models import Dealer


class Bottler(models.Model):
    bottler_name = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Brand(models.Model):
    brand_code = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50,unique=True)
    bottler_id = models.ForeignKey(Bottler, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserBrand(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        data = {
            "id": self.id,
            "brand_id": self.brand_id.id,
            "user_id": self.user_id.id,
            "quantity": self.quantity,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        return data


class DealerBrand(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        data = {
            "id": self.id,
            "brand_id": self.brand_id.id,
            "dealer_id": self.dealer_id.id,
            "brand_name": self.brand_id.brand_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        return data
