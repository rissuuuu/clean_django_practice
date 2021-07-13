from django.db import models
from user.models import User
from location.models import District, Province


class ResidentialKind(models.TextChoices):
    TENANT = "tenant"
    LANDLORD = "landlord"


class Gender(models.TextChoices):
    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"


class CustomerKind(models.TextChoices):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"


class Relation(models.TextChoices):
    FATHER = "father"
    MOTHER = "mother"


class KycUpdatedStatus(models.TextChoices):
    pending = "pending"
    submitted = "submitted"
    rejected = "rejected"
    accepted = "accepted"


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=50, choices=Gender.choices)
    mobile = models.BigIntegerField()
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_kind = models.CharField(max_length=20, choices=CustomerKind.choices)
    picture = models.URLField(null=True, blank=True)
    kyc_updated = models.CharField(
        max_length=15, choices=KycUpdatedStatus.choices, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        data = {
            "first_name": self.first_name,
            "midddle name": self.middle_name,
            "last_name": self.last_name,
            "gender":self.gender,
            "phone_number": self.mobile,
            "customer_kind": self.customer_kind,
            "kyc_updated":self.kyc_updated
        }
        return data


class Residential(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    kind = models.CharField(
        max_length=20, default="tenant", choices=ResidentialKind.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        data = {
            "customer_id": self.customer_id.id,
            "kind": self.kind,
        }
        return data


class Commercial(models.Model):
    proprieter_name = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        data = {
            "proprieter_name": self.proprieter_name,
            "customer_id": self.customer_id.id,
        }
        return data


class CustomerKyc(models.Model):
    caste = models.CharField(max_length=20)
    dob_english = models.DateField()
    dob_nepali = models.DateField()
    pan_no = models.BigIntegerField(null=True, blank=True)
    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE)
    is_kyc_verified = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="province"
    )
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="district"
    )
    citizenship = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerDocuments(models.Model):
    citizenship = models.ImageField(upload_to="customerdocs/", null=True, blank=True)
    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerFamily(models.Model):
    relation = models.CharField(max_length=20, choices=Relation.choices)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
