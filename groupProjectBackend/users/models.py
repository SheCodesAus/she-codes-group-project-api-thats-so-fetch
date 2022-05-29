from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from articles.models import Category


class CustomUser(AbstractUser):
    is_mentor = models.BooleanField(default=False, null=True, blank=True)
    is_student = models.BooleanField(default=False, null=True, blank=True)
    profile_photo = models.URLField(null=True, blank=True)
    banner_photo = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    social_link = models.URLField(max_length=255, null=True, blank=True, unique=True)
    bio = models.CharField(max_length=600, blank=True, null=True) 
    coffee = models.BooleanField(default=False, null=True, blank=True)
    mentoring = models.BooleanField(default=False, null=True, blank=True)
    tutoring = models.BooleanField(default=False, null=True, blank=True)
    public_speaking = models.BooleanField(default=False, null=True, blank=True)
    skills = models.ManyToManyField(Category, related_name='skills')
    
    def __str__(self):
        return self.username
     


