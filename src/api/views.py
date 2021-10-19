from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AuthUser
from .serializers import UserListSerializer, UserCreateSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = UserListSerializer


class UserCreateViewSet(viewsets.ModelViewSet):
    # queryset = AuthUser.objects.all()
    serializer_class = UserCreateSerializer