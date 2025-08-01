from rest_framework import serializers
from offers_app.models import Offer, OfferDetails
from rest_framework.reverse import reverse
from rest_framework import fields
from rest_framework.exceptions import ValidationError

class OfferDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = OfferDetails
        fields = [
                  "id", 
                  "title", 
                  "revisions", 
                  "delivery_time_in_days", 
                  "price", 
                  "features",
                  "offer_type"] #this is hwat I can see
        
class OfferDetailsLinkSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = OfferDetails
        fields = ["id", "url"]
    
    def get_url(self, obj):
        request = self.context.get("request")
        return reverse("offerdetails-detail", args=[obj.id], request=request)

class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailsSerializer(many=True)
    user_details = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
                  "id",
                  "user",
                  "title", 
                  "image", 
                  "description",
                  "created_at",
                  "updated_at",
                  "details",
                  "min_price",
                  "min_delivery_time",
                  "user_details"
                  ]
        read_only_fields = ["id", "user", "user_details", "min_price", "min_delivery_time"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get("view")
        if view and hasattr(view, "action") and view.action == "retrieve":
            # Remove user_details from output if we're in retrieve view
            self.fields.pop("user_details", None)

    def get_user_details(self, obj):
        user = obj.user
        view = self.context.get("view")

        if view and hasattr(view, 'action') and view.action != 'retrieve':
            return {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username
            }

    def get_user(self, obj):
        return obj.user.id
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")

        if request and request.method == "GET":
            # Read: minimal serializer with ID und URL
            fields["details"] = OfferDetailsLinkSerializer(many=True, read_only=True)
        else:
            # Write: full serializer with all details
            fields["details"] = OfferDetailsSerializer(many=True)
        return fields
    
    def validate_details(self, value):
        if len(value) != 3:
            raise ValidationError("Exactly 3 details are required.")
        return value


    def create(self, validated_data):
        details_data = validated_data.pop("details")
        request = self.context.get("request")

        validated_data["user"] = request.user
        validated_data["min_price"] = min(d["price"] for d in details_data)
        validated_data["min_delivery_time"] = min(d["delivery_time_in_days"] for d in details_data)

        offer = Offer.objects.create(**validated_data)

        for detail_data in details_data:
            OfferDetails.objects.create(offer=offer, **detail_data)
        
        return offer
    

    def update(self, instance, validated_data):
        details_data = validated_data.pop("details", [])
        existing_details = {detail.id: detail for detail in instance.details.all()}

        # Update main Offer fields
        instance = super().update(instance, validated_data)

        for detail_data in details_data:
            detail_id = detail_data.get("id")

            if detail_id and detail_id in existing_details:
                # Update existing detail
                detail_instance = existing_details[detail_id]
                for attr, value in detail_data.items():
                    setattr(detail_instance, attr, value)
                detail_instance.save()
                
            else:
                # Create new detail
                OfferDetails.objects.create(offer=instance, **detail_data)

        # Recalculate min_price and min_delivery_time
        all_details = instance.details.all()
        if all_details.exists():
            instance.min_price = min(d.price for d in all_details)
            instance.min_delivery_time = min(d.delivery_time_in_days for d in all_details)
        instance.save()

        return instance