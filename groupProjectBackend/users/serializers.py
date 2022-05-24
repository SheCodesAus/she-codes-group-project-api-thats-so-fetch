
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# This is the create profile section?
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    is_mentor = serializers.BooleanField()
    is_student = serializers.BooleanField()
    profile_photo = serializers.URLField()
    banner_photo = serializers.URLField()
    location = serializers.CharField(max_length=30)
    social_link = serializers.URLField()
    bio = serializers.CharField(max_length=600)

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)


class CustomUserDetailSerializer(CustomUserSerializer):
        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.is_mentor = validated_data.get('is_mentor', instance.is_mentor)
            instance.is_student = validated_data.get('is_student', instance.is_student)
            instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
            instance.banner_photo = validated_data.get('banner_photo', instance.banner_photo)
            instance.location = validated_data.get('location', instance.location)
            instance.social_link = validated_data.get('social_link', instance.social_link)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.save()
            return instance

# Create a user account
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2', 'is_mentor', 'is_student', 'profile_photo', 'banner_photo', 'location', 'social_link', 'bio')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'], 
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
