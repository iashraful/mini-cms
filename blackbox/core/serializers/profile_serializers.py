from datetime import datetime
from django.contrib.auth.models import User
from drf_role.models import Role
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blackbox.core.models.profile import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'type')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'role', 'date_of_birth', 'gender', 'mobile', 'address')


class ProfileDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'name')


class ProfileLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name',)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ('username', 'password')


class RegistrationSerializer(serializers.Serializer):
    role = serializers.IntegerField(required=False)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    gender = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')

        user_by_username = User.objects.filter(username=username).first()
        user_by_email = User.objects.filter(email=email).first()
        if user_by_username:
            raise ValidationError({"username": ["username already exists."]})
        if user_by_email:
            raise ValidationError({"email": ["email already exists."]})
        return attrs

    class Meta:
        fields = ('role', 'username', 'password', 'email', 'gender')
