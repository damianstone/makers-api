from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
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
    
    # Change the default permissions for the create endpoint (register) so it doesn't require authentication
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [permission() for permission in self.permission_classes]
    
    # List users in startups or corporations
    def list(self, request):
        queryset = self.get_queryset()
        
        # getting query params
        company_type = request.query_params.get('company_type', None)
        company_industry = request.query_params.get('company_industry', None)
        
        # filter using queries 
        if company_type is not None:
            queryset = queryset.filter(company_type=company_type)
        
        if company_industry is not None:
            queryset = queryset.filter(company_industry=company_industry)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    # Register
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
        except:
            message = {"detail": "Email already exist"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data)


    # Update properties in the user model
    def partial_update(self, request, pk=None):
        current_user = request.user
        
        try:
            user = models.User.objects.get(pk=pk)
        except:
            message = {"detail": "User does not exist"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        if current_user.id != user.id:
            message = {"detail": "Not authorized"}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED,)
        
        fields_serializer = serializers.CreateProfileSerializer(data=request.data)
        fields_serializer.is_valid(raise_exception=True)
        
        for key, value in  fields_serializer.validated_data.items():
            setattr(user, key, value)
        
        user.has_profile = True
        user.save()
        profile_serializer = self.serializer_class(user, many=False)
        return Response(profile_serializer.data)


class InvitationViewSet(GenericViewSet):
    queryset = models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer
    permission_classes = [IsAuthenticated]
    
    # List all the invitations in the database just for admins (superusers)
    # def get_permissions(self):
    #     if self.action == "list":
    #         return [IsAdminUser()]
    #     return [permission() for permission in self.permission_classes]
    
    # List all the invitations in the database
    def list(self, request):
        invitations = models.Invitation.objects.all()
        ordered_invitations = invitations.order_by(
        "-sent_at"
        )
        serializer = serializers.InvitationSerializer(ordered_invitations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["post"], url_path="actions/send-invitation")
    def send_invitation(self, request, pk=None):
        current_user = request.user
        message = request.data["message"]
        interest = request.data["interest"]
        
        try: 
            invited_user = models.User.objects.get(pk=pk)
        except:
            message = {"detail": "User does not exist"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        if current_user.id == invited_user.id:
            message = {"detail": "You cannot invite yourself"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST,)
        
        if not current_user.has_profile:
            message = {"details": "You need to complete your details to send invitations!"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
            
        invitation = models.Invitation.objects.create(sender=current_user, receiver=invited_user, message=message, interest=interest)   
        serializer = serializers.InvitationSerializer(invitation, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="actions/my-invitations")
    def list_my_invitations(self, request):
        user = request.user
        invitations = user.invitations_received.all()
        ordered_invitations = invitations.order_by(
        "-sent_at"
    )
        serializer = serializers.InvitationSerializer(ordered_invitations, many=True)
        return Response(serializer.data)
    