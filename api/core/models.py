from django.contrib.auth.models import AbstractUser
from django.db import models

from core.mixins.models import BaseModelUUID, BaseModelCreatedData


def custom_upload_to(instance, filename):
    return "user_{0}/{1}".format(
        instance.user.id,
        filename,
    )


class User(AbstractUser, BaseModelUUID):
    name = models.CharField(
        blank=True,
        max_length=255,
    )
    first_name = None
    last_name = None
    email = models.EmailField()
    username = models.CharField(
        blank=True,
        max_length=255,
        unique=True,
    )
    picture = models.ImageField(
        upload_to=custom_upload_to,
        null=True,
        blank=True,
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
