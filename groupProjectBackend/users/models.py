# from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


#PermissionsMixin adds in user to django permision framework 



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    profile_photo = models.ImageField(null=True, upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png')
    banner_photo = models.ImageField(null=True, blank=True, upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png')
    linkedin_url = models.CharField(max_length=255, null=True, blank=True, unique=True)
    website_url = models.CharField(max_length=255, null=True, blank=True, unique=True)
    social_media = models.CharField(max_length=255, null=True, blank=True, unique=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

#defining that we are using custom account manager  
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

