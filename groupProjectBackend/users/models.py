from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# the below imports are from the django.contrib.auth.models (line 5) 
# AbstractBaseUser, PermissionsMixin, BaseUserManager

#spelling_error

#PermissionsMixin adds in user to django permision framework 

# class CustomAccountManager(BaseUserManager):
#     def create_superuser(self, email, user_name, first_name, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(email, user_name, first_name, password, **other_fields)

#     def create_user(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

class CustomUser(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    profile_photo = models.URLField(null=True, blank=True)
    banner_photo = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    social_link = models.URLField(max_length=255, null=True, blank=True, unique=True)
    bio = models.CharField(max_length=600, blank=True, null=True) 
    coffee = models.BooleanField(default=False, null=True, blank=True)
    mentoring = models.BooleanField(default=False, null=True, blank=True)
    tutoring = models.BooleanField(default=False, null=True, blank=True)
    public_speaking = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.username
     
#defining that we are using custom account manager  
    # objects = CustomAccountManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['user_name', 'first_name']

    # def __str__(self):
    #     return self.user_name


