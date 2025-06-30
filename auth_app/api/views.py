from rest_framework import generics
from auth_app.models import Profile
from .serializer import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from phonenumber_field.phonenumber import PhoneNumber


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                "token": token.key,
                "username": saved_account.username,
                "email": saved_account.email,
                "user_id": saved_account.id
            }
            return Response(data, status=status.HTTP_201_CREATED)

        field_names = [
            "username", "email", "password", "repeated_password", "type"
        ]
        for field in field_names:
            if field in serializer.errors:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

