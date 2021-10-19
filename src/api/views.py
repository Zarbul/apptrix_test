from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import AuthUser
from .serializers import UserListSerializer, UserCreateSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name', 'gender')


class UserCreateViewSet(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
