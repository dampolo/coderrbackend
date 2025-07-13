from rest_framework import serializers
from orders_app.models import Order
from offers_app.models import Offer, OfferDetails
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    offer_detail_id = serializers.IntegerField(write_only=True, required=True) 
    #write_only=True - This field is used when sending data to the API (e.g., in POST or PUT requests), but it will not appear in the response output.
    
    class Meta:
        model = Order
        fields = [
            "id",
            "customer_user",
            "business_user",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
            "status",
            "created_at",
            "updated_at",
            "offer_detail_id"
        ]
         # Make everything that's filled in automatically read-only
         # #Djanog will ignort this fiels in input
        read_only_fields = [
            "id",
            "customer_user",
            "business_user",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
            "status",
            "created_at",
            "updated_at"
        ]
    
    def create(self, validated_data):
        offer_detail_id = validated_data.pop("offer_detail_id")
        offer_detail = get_object_or_404(OfferDetails, id=offer_detail_id)
        offer = offer_detail.offer  # get parent Offer object

        request = self.context.get("request")
        customer_user = request.user if request else None

        order = Order.objects.create(
            customer_user=customer_user,
            business_user=offer.user,
            title=offer_detail.title,
            revisions=offer_detail.revisions,
            delivery_time_in_days=offer_detail.delivery_time_in_days,
            price=offer_detail.price,
            features=offer_detail.features,
            offer_type=offer_detail.offer_type,
            status='pending',  # or default value
            # add any other fields you're using
        )
        return order

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)