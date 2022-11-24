from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('entrypoint', include('app_ti.links')),
    path('admin/', admin.site.urls),
]