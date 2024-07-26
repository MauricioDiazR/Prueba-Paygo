from rest_framework import serializers
from roles.models import Role, Permission, User, LANGUAGE_CHOICES, STYLE_CHOICES

class PermissionSerializer(serializers.Serializer):
    
    name = serializers.CharField(allow_blank=False,allow_null=False)
    class Meta:
        model = Permission
        fields = ['id','name']
    def create(self, validated_data):
        return Permission.objects.create(**validated_data)

   
class RoleSerializer(serializers.ModelSerializer):
    name= serializers.CharField(allow_blank=False,allow_null=False)

    active=serializers.BooleanField(default=True)
    
    class Meta:
        model = Role
        fields = ['id','name', 'permission','active']

    def create(self, validated_data):
        permission = validated_data.pop('permission')
        role = Role.objects.create(**validated_data)
        role.permission.set(permission)
        return role

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.permission = validated_data.get('permission', instance.permission)
        instance.active = validated_data.get('active', instance.active)
        return instance        


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_blank=False,allow_null=False)
    role=serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)
    password= serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','name', 'role','password']
    
    def create(self, validated_data):
        role= validated_data.pop('role')
        password= validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.role.set(role)
        user.save()
        return user
    
    def verique_role(self,value):
        if not Role.objects.filter(id=value).exists():
            raise serializers.ValidationError("No existe el rol")
        return value



    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        role = validated_data.pop('role', None)
        instance.name = validated_data.get('name', instance.name)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        if role is not None:
            instance.role.set(role)
        return instance