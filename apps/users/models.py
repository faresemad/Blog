import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "phone"]

    class Meta:
        verbose_name_plural = "Users"
        indexes = [
            models.Index(fields=["id", "username"]),
        ]
