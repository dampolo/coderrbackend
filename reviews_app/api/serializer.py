from rest_framework import serializers
from reviews_app.models import Review
from django.shortcuts import get_object_or_404

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
            "reviewer"
        ]

    def get_reviewer(self, obj):
        user = obj.reviewer
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }        

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["reviewer"] = request.user
        return super().create(validated_data)