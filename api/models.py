import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.contrib.postgres.fields import ArrayField
from model_utils import Choices

from api.data.choices import INDUSTRY_CHOICES, INTEREST_CHOICES, TYPE_CHOICES


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)
    has_profile = models.BooleanField(default=False)

    meeting_link = models.CharField(max_length=300, null=True)
    position = models.CharField(max_length=300, null=True)
    photo = models.ImageField(null=True, blank=True)

    company_photo = models.ImageField(null=True, blank=True)
    company_name = models.CharField(max_length=300, null=True)
    company_description = models.CharField(max_length=300, null=True)
    company_valuation = models.CharField(max_length=300, null=True)
    company_employees = models.CharField(max_length=300, null=True)
    company_investment = models.CharField(max_length=300, null=True)

    company_type = models.CharField(
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES.startup,
        max_length=50,
        null=True,
        blank=True,
    )

    company_industry = models.CharField(
        choices=INDUSTRY_CHOICES,
        default=INDUSTRY_CHOICES.agriculture,
        max_length=50,
        null=True,
        blank=True,
    )

    interests = ArrayField(
        models.CharField(
            choices=INTEREST_CHOICES,
            default=INTEREST_CHOICES.collaboration,
            max_length=50,
            null=True,
            blank=True,
        ),
        blank=True,
        default=list,
    )

    USERNAME_FIELD = "email"

    # requred for creating user
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        return self.firstname + self.lastname
    
    def get_interests_display(self):
        return [dict(INTEREST_CHOICES).get(interest) for interest in self.interests]

    def delete(self):
        self.photo.delete(save=False)
        super().delete()


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
        User, related_name="invitations_sent", default=None, on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name="invitations_received",
        default=None,
        on_delete=models.CASCADE,
    )
    message = models.CharField(max_length=500, null=True)
    sent_at = models.DateTimeField(default=timezone.now)
    interest = models.CharField(
        choices=INTEREST_CHOICES,
        default=INTEREST_CHOICES.collaboration,
        max_length=50,
        null=False,
        blank=False,
    )
