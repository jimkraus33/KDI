from django.urls import path
from . import views


urlpatterns = [
    path('clients/', views.clients, name="clients"),
    path('create_clients/', views.create_clients, name="create_clients"),
    path('view_clients/<int:pk>/', views.view_clients, name="view_clients"),
    path('update_clients/<int:pk>/', views.update_clients, name="update_clients"),
    path('delete_clients/<int:pk>/', views.delete_clients, name="delete_clients"),
]
