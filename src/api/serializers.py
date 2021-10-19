from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from src.api.models import AuthUser


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('first_name', 'last_name', 'gender')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = AuthUser
        fields = ('email', 'password', 'first_name', 'last_name', 'gender', 'avatar')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserCreateSerializer, self).create(validated_data)
