from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000 and view function: app_home
    path('', views.app_home, name='app_home'),
    path('/a', views.app_a, name='app_home'),
    path('/', views.app_b, name='app_home'),
]
# localhost:8000/entrypoint/
# localhost:8000/entrypoint
# localhost:8000/entrypoint/a