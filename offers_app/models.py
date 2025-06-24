from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Offer(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="offer")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="design_packages/", null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class OfferDetails(models.Model):
    class OfferType(models.TextChoices):
        BASIC = "basic", _("Basic")
        STANDARD = "standard", _("Standard")
        PREMIUM = "premium", _("Premium")

    offer = models.ForeignKey(Offer, related_name='details', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    revisions = models.PositiveIntegerField(default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField()
    offer_type = models.CharField(max_length=10, choices=OfferType, default=OfferType.BASIC)

    def __str__(self):
        return f"{self.offer_type} - {self.title}"
    
