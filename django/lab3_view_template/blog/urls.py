from django.urls import path
from . import views

app_name = "blog"   #thêm app_name để dùng namespace

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('year/<int:year>/', views.year_archive, name='year_archive'),
]
