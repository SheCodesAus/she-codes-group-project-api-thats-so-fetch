from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    avatar = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

