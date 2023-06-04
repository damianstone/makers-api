from rest_framework import serializers
from api import models
from rest_framework_simplejwt.tokens import RefreshToken

from api.data.choices import INDUSTRY_CHOICES, INTEREST_CHOICES, TYPE_CHOICES


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


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        exclude = [
            "last_login",
            "is_superuser",
            "password",
            "user_permissions",
            "groups",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class UserProfileSerializer(serializers.ModelSerializer):
    company_type = serializers.CharField(
        source="get_company_type_display", required=True, allow_null=False
    )
    company_industry = serializers.CharField(
        source="get_company_industry_display", required=True, allow_null=False
    )

    interests = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        exclude = [
            "last_login",
            "is_superuser",
            "password",
            "user_permissions",
            "groups",
        ]
        
    def get_interests(self, obj):
        return obj.get_interests_display()



class UserSenderInvitationSerializer(serializers.ModelSerializer):
    company_type = serializers.CharField(
        source="get_company_type_display", required=True, allow_null=False
    )
    company_industry = serializers.CharField(
        source="get_company_industry_display", required=True, allow_null=False
    )

    class Meta:
        model = models.User
        exclude = [
            "last_login",
            "is_superuser",
            "password",
            "user_permissions",
            "groups",
            "interests",
        ]


class InvitationSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Invitation
        fields = "__all__"

    def get_sender(self, invitation):
        sender_profile = UserSenderInvitationSerializer(
            invitation.sender, many=False)
        return sender_profile.data


# Serializer used to check the minimum requeriments when creating the user profile
class CreateProfileSerializer(serializers.Serializer):
    firstname = serializers.CharField(required=True, allow_null=False)
    lastname = serializers.CharField(required=True, allow_null=False)
    position = serializers.CharField(required=True, allow_null=False)
    company_name = serializers.CharField(required=True, allow_null=False)
    company_description = serializers.CharField(
        required=True, allow_null=False)
    meeting_link = serializers.CharField(required=False, allow_null=True)
    company_valuation = serializers.CharField(required=False, allow_null=True)
    company_employees = serializers.CharField(required=False, allow_null=True)
    company_investment = serializers.CharField(required=False, allow_null=True)

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

    interests = serializers.ListField(
        child=ChoicesField(
            choices=INTEREST_CHOICES,
            required=False,
            allow_null=False,
        ),
        required=False,
        default=list,
    )
