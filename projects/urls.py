from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('create_projects/', views.create_projects, name="create_projects"),
    path('view_projects/<int:pk>/', views.view_projects, name="view_projects"),
    path('update_projects/<int:pk>/', views.update_projects, name="update_projects"),
    path('delete_projects/<int:pk>/', views.delete_projects, name="delete_projects"),
]
