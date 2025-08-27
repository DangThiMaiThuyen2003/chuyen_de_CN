from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("2003/", views.special_case_2003),
    path("<int:year>/", views.year_archive),
    path("<int:year>/<int:month>/", views.month_archive),
    path("<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    path("cbv/", include("cbvapp.urls")), 
]
