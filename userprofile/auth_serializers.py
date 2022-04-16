from account.models import User
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from .models import UserProfile

user_model = get_user_model()
    
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = user_model 
        fields = ['id', 'username', 'email', 'is_active','password', 'created', 'updated','is_staff']
        read_only_field = ['is_active', 'created', 'updated']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = UserProfile
        fields = ['id','user', 'street_address','city','postal_code','country', 'created', 'updated','created_by_admin_user',]
        read_only_field = [ 'created', 'updated']
        