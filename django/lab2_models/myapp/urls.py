from django.urls import path
from myapp.views import entry_list, entry_delete, entry_detail, author_detail

app_name = 'myapp'
urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('delete/<int:pk>/', entry_delete, name='entry_delete'),
    path('entry/<int:pk>/', entry_detail, name='entry_detail'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
]