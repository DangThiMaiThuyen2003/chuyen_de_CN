from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("now/", views.current_datetime, name="current-datetime"),
    path("simple404/", views.simple_404_view, name="simple-404"),
    path("raise404/", views.raise_404_view, name="raise-404"),
    path("created/", views.created_view, name="created"),
]
