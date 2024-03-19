from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name="contacts"),
    path('create_contacts/', views.create_contacts, name="create_contacts"),
    path('view_contacts/<int:pk>/', views.view_contacts, name="view_contacts"),
    path('update_contact/<int:pk>/', views.update_contacts, name="update_contacts"),
    path('delete_contacts/<int:pk>/', views.delete_contacts, name="delete_contacts"),
]
