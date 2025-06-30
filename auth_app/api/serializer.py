from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
from auth_app.models import Profile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import MinLengthValidator
from auth_app.validators import CustomPhoneValidator, CustomPasswordValidator
from django.contrib.auth import authenticate



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    repeated_password = serializers.CharField(write_only=True, trim_whitespace=False)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

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
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_username(self, value):
        value = value.lower()
        try:
            MinLengthValidator(3)(value)
        except DjangoValidationError as error:
            raise serializers.ValidationError(error.messages)
            # Check uniqueness
        if Profile.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("This username exists already.")
        return value
    
    def validate_password(self, value):
        repeated_pw = self.initial_data.get("repeated_password")        
        # Custom complexity validation
        try:
            CustomPasswordValidator().validate(value)
        except DjangoValidationError as error:
            raise serializers.ValidationError(error.messages)
        
        if repeated_pw and value != repeated_pw:
            raise serializers.ValidationError("Passwords don't match.")
        return value
    
    def validate_email(self, value):
        value = value.lower()
        if Profile.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email exists already.")
        return value
    
    def create(self, validated_data):
        validated_data.pop("repeated_password")
        password = validated_data.pop("password")
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        return user
