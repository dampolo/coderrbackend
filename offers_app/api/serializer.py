from rest_framework import serializers
from offers_app.models import Offer, OfferDetails
from django.conf import settings

class OfferDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetails
        fields = ["title", 
                  "revisions", 
                  "delivery_time_in_days", 
                  "price", 
                  "features"] #this is hwat I can see

class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailsSerializer(many=True)
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
                  "id",
                  "user",
                  "title", 
                  "image", 
                  "description",
                  "created_at",
                  "details",
                  "min_price",
                  "min_delivery_time",
                  "user_details"
                  ]
        
        read_only_fields = ["user_details", "min_price", "min_delivery_time"]

    def get_user_details(self, obj):
        print(obj.user.last_name)
        return {
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "username": obj.user.username
        }
        
    def create(self, validated_data):
        details_data = validated_data.pop("details")

        validated_data["min_price"] = min(d["price"] for d in details_data)
        validated_data["min_delivery_time"] = min(d["delivery_time_in_days"] for d in details_data)

        offer = Offer.objects.create(**validated_data)

        for detail_data in details_data:
            OfferDetails.objects.create(offer=offer, **detail_data)
        
        return offer