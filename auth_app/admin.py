from django.contrib import admin
from auth_app.models import Profile
from offers_app.models import Offer, OfferDetails

# Register your models here.

class CustomProfile(admin.ModelAdmin):
    list_display = ["username", "type", "email"]


admin.site.register(Profile, CustomProfile)
admin.site.register(Offer, OfferDetails)

