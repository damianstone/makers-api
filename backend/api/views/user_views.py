from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api import models, serializers
from django.contrib.auth.hashers import make_password
import re

# simple json token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = serializers.UserSerializer(self.user).data
        for key, value in serializer.items():
            data[key] = value

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    


def validate_email_address(email_address):
    pattern = r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$"
    if not re.search(pattern, email_address):
       print(f"The email address {email_address} is not valid")
       return False
    return True



class UserModelViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request): 
        data = request.data
        email = data["email"]
        password = data["password"]
        repeated_password = data["repeated_password"]
        validation_email = validate_email_address(email)
        
        if not validation_email:
            message = {"detail": f"The email address {email} is not valid"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        if password != repeated_password:
            message = {"detail": "Your password does not match"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            user = models.User.objects.create(
                email=email, password=make_password(password)
            )
            serializer = serializers.UserSerializer(user, many=False)
            return Response(serializer.data)
        except:
            message = {"detail": "Email already exist"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    # register user
    @action(detail=False, methods=["post"], url_path=r"actions/create-profile")
    def create_profile(self, request):
        user = request.user
        fields_serializer = serializers.CreateProfileSerializer(data=request.data)
        fields_serializer.is_valid(raise_exception=True)
        
        # profile_data = fields_serializer.validated_data
        # profile = models.Profile.objects.create(user=user, **profile_data)
        
        user.save()
        profile_serializer = serializers.UserSerializer(user)
        return Response(profile_serializer.data)

    def update(self, request, pk=None):
        pass
