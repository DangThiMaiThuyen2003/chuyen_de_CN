from rest_framework import serializers
from apiApp.models.role import Role, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'description']

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Permission.objects.all(), write_only=True, source='permissions')

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions', 'permission_ids']
        extra_kwargs = {
            'description': {'required': True}
        }
        
    def validate_name(self, value):
        # Kiểm tra độ dài tên role
        if len(value) < 3:
            raise serializers.ValidationError("Tên role phải có ít nhất 3 ký tự")

        # Khi update, không kiểm tra trùng với chính nó
        if self.instance and self.instance.name == value:
            return value
        if Role.objects.filter(name=value).exists():
            raise serializers.ValidationError("Tên role này đã tồn tại")

        return value

    
    
