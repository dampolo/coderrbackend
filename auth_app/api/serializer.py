from rest_framework import serializers
from auth_app.models import Profile
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import MinLengthValidator
from auth_app.validators import CustomPasswordValidator
from django.contrib.auth import authenticate
from django.utils.timezone import now

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError({
                "message": "Oops! Wrong password or username. Please try again."  # <-- your custom message
            })

        data["user"] = user
        return data

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    repeated_password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "password",
            "repeated_password",
            "first_name",
            "last_name",
            "type",
        ]
    
    def validate_password(self, value):
        if value != self.initial_data.get("repeated_password"):
            raise serializers.ValidationError("Passwords do not match.")
        return value
    
    def create(self, validated_data):
        validated_data.pop("repeated_password")
        password = validated_data.pop("password")
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            "user",
            "username",
            "first_name",
            "last_name",
            "file",
            "location",
            "tel",
            "description",
            "working_hours",
            "type",
            "email",
            "created_at"
        ]

class ProfileCustomSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            "user",
            "username",
            "first_name",
            "last_name",
            "file",
            "updated_at",
            "type"
        ]

        
class ProfileBusinessSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            "user",
            "username",
            "first_name",
            "last_name",
            "file",
            "location",
            "tel",
            "description",
            "working_hours",
            "type"
        ]