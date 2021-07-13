from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_active = models.BooleanField(default=True,null=False)
    is_admin = models.BooleanField(default=False, null=False)
    is_dealer = models.BooleanField(default=False, null=False)
    is_customer = models.BooleanField(default=False, null=False)
    is_bottler = models.BooleanField(default=False, null=False)
    middle_name = models.CharField(max_length=20,blank=True)
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]

