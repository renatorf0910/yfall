from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', views.UserList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
