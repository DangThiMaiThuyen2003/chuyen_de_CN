from rest_framework import viewsets
from apiApp.models.role import Role, Permission
from apiApp.serializers.role_serializers import RoleSerializer, PermissionSerializer
from apiApp.utils.cache_utils import cache_response
from django.core.cache import cache
from django.conf import settings

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
    @cache_response(timeout=settings.CACHE_TTL)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @cache_response(timeout=settings.CACHE_TTL)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete_pattern('*roles*')
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete_pattern('*roles*')
        return response
    
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete_pattern('*roles*')
        return response

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
