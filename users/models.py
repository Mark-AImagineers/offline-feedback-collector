from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
    
SUBSCRIPTION_FREE = 0
SUBSCRIPTION_BASIC = 1
SUBSCRIPTION_PRO = 2
SUBSCRIPTION_ENTERPRISE = 3

SUBSCRIPTION_CHOICES = [
    (SUBSCRIPTION_FREE, "Free"),
    (SUBSCRIPTION_BASIC, "Basic"),
    (SUBSCRIPTION_PRO, "Pro"),
    (SUBSCRIPTION_ENTERPRISE, "Enterprise"),
]

class EmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    subscription_expires = models.DateTimeField(null=True, blank=True, help_text="When the current subscription level expries. Auto-resets to Free")

    subscription_level = models.PositiveSmallIntegerField(
        choices=SUBSCRIPTION_CHOICES,
        default=SUBSCRIPTION_FREE,
        help_text="0=Free, 1=Basic, 2=Pro, 3=Enterprise"
    )

    def save(self, *args, **kwargs):
        if self.subscription_expires and timezone.now() > self.subscription_expries:
            self.subscription_level = SUBSCRIPTION_FREE
            self.subscription_expires = None
            super().save(*args, **kwargs)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email