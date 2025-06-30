from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Order(models.Model):
    class OfferType(models.TextChoices):
        BASIC = "basic", _("Basic")
        STANDARD = "standard", _("Standard")
        PREMIUM = "premium", _("Premium")
    
    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", _("In Progress")
        COMPLETED = "completed", _("Completed")
        CANCELLED = "cancelled", _("Cancelled")

    
    customer_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_offers"
    )

    business_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="business_offers"
    )

    title = models.CharField(max_length=255)
    revisions = models.PositiveIntegerField(default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list)
    offer_type = models.CharField(
        max_length=10, 
        choices=OfferType, 
        default=Status.IN_PROGRESS)
    status = models.CharField(
        max_length=15,
        choices=Status,
        default=Status.IN_PROGRESS
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} + ({self.customer_user} + {self.business_user})"