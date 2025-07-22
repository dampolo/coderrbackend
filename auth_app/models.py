from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Profile(AbstractUser):
    class ProfileType(models.TextChoices):
        CUSTOMER = "customer", _("Customer")
        BUSINESS = "business", _("Business")

    email = models.EmailField(max_length=150, unique=True, default=None)
    file = models.ImageField(upload_to='uploads/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, default="")
    tel = PhoneNumberField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    working_hours = models.CharField(max_length=50, blank=True, default="")
    type = models.CharField(
        max_length=10,
        choices=ProfileType,
        default=ProfileType.CUSTOMER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username