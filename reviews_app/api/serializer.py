from rest_framework import serializers
from reviews_app.models import Review
from auth_app.models import Profile
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError as DjangoValidationError

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "reviewer",
            "business_user"
        ]

    def get_reviewer(self, obj):
        user = obj.reviewer
        return user.id
    
    
    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        business_user = validated_data.get("business_user")

        if Review.objects.filter(reviewer=user, business_user=business_user).exists():
            raise serializers.ValidationError("You have already reviewed this user.")
            
        validated_data["reviewer"] = request.user
        return super().create(validated_data)