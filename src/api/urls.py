from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.UserListViewSet.as_view({'get': 'list'}, name='user-list')),
    path('clients/create/', views.UserCreateViewSet.as_view({'post': 'create'})),
]
