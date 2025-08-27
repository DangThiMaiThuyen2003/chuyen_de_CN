from django.urls import path
from .views import AboutView, AsyncHelloView, BookListView
from . import views

app_name = "cbvapp"

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("async-hello/", AsyncHelloView.as_view(), name="async-hello"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("hello-template/", views.hello_template, name="hello-template"),
]
