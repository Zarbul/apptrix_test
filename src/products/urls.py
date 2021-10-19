from django.urls import path

from . import parser

urlpatterns = [
    path('', parser.parser),
    # path('list/', views.UserListViewSet.as_view({'get': 'list'})),
    # path('clients/create/', views.UserCreateViewSet.as_view({'post': 'create'})),
]
