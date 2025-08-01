from rest_framework import generics
from auth_app.models import Profile
from .serializer import RegistrationSerializer, LoginSerializer, ProfileSerializer, ProfileCustomSerializer, ProfileBusinessSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from auth_app.permissions import IsOwner
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from django.utils.crypto import get_random_string
from phonenumber_field.phonenumber import PhoneNumber
from django.utils.timezone import now
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

class CustomLoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data["user"]

             # Update last_login manually since you're not calling login()
            user.last_login = now()
            user.save(update_fields=["last_login"])

            token, created = Token.objects.get_or_create(user=user)
            data = {
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id,
            }
            return Response(data, status=status.HTTP_200_OK)
        field_names = [
            "username", "password"
        ]
        for field in field_names:
            if field in serializer.errors:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(ModelViewSet):
    permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfilesCustomerViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfileCustomSerializer    
    def get_queryset(self):
        return Profile.objects.filter(type="customer")

class ProfilesBusinessViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfileBusinessSerializer
    def get_queryset(self):
        return Profile.objects.filter(type="business")