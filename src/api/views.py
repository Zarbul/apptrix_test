from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AuthUser
from .serializers import UserListSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = UserListSerializer