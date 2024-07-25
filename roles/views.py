from urllib import response
from roles.models import Permission, Role, User
from roles.serializers import PermissionSerializer, RoleSerializer, UserSerializer
from rest_framework import mixins,generics,status
from rest_framework.response import Response
from django.shortcuts import render
from roles.permission import IsOwnerOrReadOnly
from rest_framework import permissions

# Create your views here.
class PermissionList(mixins.ListModelMixin,mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()

class PermissionDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class  RoleList(mixins.ListModelMixin,mixins.CreateModelMixin,
                     generics.GenericAPIView):
    
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()

class RoleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)   
         
    def delete(self, request, *args, **kwargs):
        role = self.get_object()
        if role.users.exists():
            role.active = False
            role.save()
            return Response({'status': 'Role deactivado'}, status=status.HTTP_200_OK)
        self.destroy(request, *args, **kwargs)
        return Response({'status': 'Role eliminado'}, status=status.HTTP_200_OK)
    
    #Verificar que el role no este asociado a un usuario, de estart asociado no se elimina
    #sino que se pone en inactivo.
class UserList(mixins.ListModelMixin, mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()

class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)