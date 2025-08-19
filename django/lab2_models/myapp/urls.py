from django.urls import path
from myapp.views import entry_list

app_name = 'myapp'
urlpatterns = [
    path('', entry_list, name='entry_list'),
]