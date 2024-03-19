from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drapes.urls')),
    path('clients/', include('clients.urls')),
    path('contacts/', include('contacts.urls')),
    path('projects/', include('projects.urls')),
]
