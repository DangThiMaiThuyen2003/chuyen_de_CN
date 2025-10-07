from django_filters import rest_framework as filters
from apiApp.models.role import Role

class RoleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    permissions = filters.NumberFilter(field_name='permissions__id')
    
    class Meta:
        model = Role
        fields = ['name', 'description', 'permissions']