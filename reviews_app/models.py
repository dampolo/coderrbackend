from django.db import models
from django.conf import settings
from orders_app.models import Offer

class Review(models.Model):
    offer = models.ForeignKey(
        Offer, 
        related_name="reviews", 
        on_delete=models.CASCADE)
    business_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="received_reviews",
        on_delete=models.CASCADE
        )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="written_reviews",
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.business_user.username} by {self.reviewer.username}"

