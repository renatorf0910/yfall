from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view({'get': 'list', 'post': 'create'})),
    path('items/<int:pk>/', views.UserList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
