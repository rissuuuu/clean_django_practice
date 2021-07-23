from django.db import models
from user.models import User
from location.models import Province, District


class Dealer(models.Model):
    first_name = models.CharField(max_length=100, null=False, default=" ")
    middle_name = models.CharField(max_length=100, null=True, blank=True, default=" ")
    last_name = models.CharField(max_length=100, null=False, default=" ")
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    mobile = models.BigIntegerField(null=False)
    email = models.EmailField(null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def to_json(self):
        data = {
            "province": self.province.id,
            "district": self.district.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "mobile": self.mobile,
            "phone": self.mobile,
            "email": self.email,
        }
        return data


class DealerDocuments(models.Model):
    dealer_document = models.URLField(null=True, blank=True)
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
