from rest_framework import serializers
from api import models
from rest_framework_simplejwt.tokens import RefreshToken

from api.data.choices import INDUSTRY_CHOICES, INTEREST_CHOICES, TYPE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        fields = "__all__"

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invitation
        fields = "__all__"
        
     
class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        if obj in self._choices:
            return self._choices[obj]
        return obj

    def to_internal_value(self, data):
        if data in self._choices:
            return getattr(self._choices, data)
        raise serializers.ValidationError(["choice not valid"])   

class CreateProfileSerializer(serializers.Serializer):
    position = serializers.CharField(required=True, allow_null=False)
    company_name = serializers.CharField(required=True, allow_null=False)
    company_description = serializers.CharField(required=True, allow_null=False)
    photo = serializers.ImageField(
        required=True, allow_null=False, max_length=None, use_url=True
    )

    company_photo = serializers.ImageField(
        required=True, allow_null=False, max_length=None, use_url=True
    )
    
    company_type = ChoicesField(
        choices=TYPE_CHOICES,
        required=False,
        allow_null=False,
    )
    
    company_industry = ChoicesField(
        choices=INDUSTRY_CHOICES,
        required=False,
        allow_null=False,
    )
    
    # interests = ChoicesField(
    #     choices=INTEREST_CHOICES,
    #     required=False,
    #     allow_null=False,
    # )
