from django.contrib import admin
from auth_app.models import Profile

# Register your models here.

class CustomProfile(admin.ModelAdmin):
    list_display = ["username", "type", "email"]


admin.site.register(Profile, CustomProfile)
