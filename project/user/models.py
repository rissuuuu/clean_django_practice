from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, null=False)
    USERNAME_FIELD = 'email'
    is_active = models.BooleanField(default=True,null=False)
    is_admin = models.BooleanField(default=False, null=False)
    is_dealer = models.BooleanField(default=False, null=False)
    is_customer = models.BooleanField(default=False, null=False)
    middle_name = models.CharField(max_length=20,blank=True)
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]
    objects = UserManager()

