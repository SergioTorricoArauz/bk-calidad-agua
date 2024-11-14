# usuarios/infrastructure/views/user_view.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from usuarios.application.services.user_service_impl import UserServiceImpl
from usuarios.infrastructure.serializers.user_serializer import UsuarioSerializer, UsuarioCrearSerializer

# Inicializar el servicio
user_service = UserServiceImpl()

class UserViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        serializer = UsuarioCrearSerializer(data=request.data)
        if serializer.is_valid():
            user = user_service.crear_usuario(
                serializer.validated_data['username'],
                serializer.validated_data['email'],
                serializer.validated_data['password'],
                serializer.validated_data['grupo']
            )
            return Response(UsuarioSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        user = user_service.obtener_usuario_por_id(int(pk))
        if user:
            return Response(UsuarioSerializer(user).data)
        return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def update(request, pk=None):
        serializer = UsuarioSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = user_service.editar_usuario(int(pk), **serializer.validated_data)
            return Response(UsuarioSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk=None):
        user_service.dar_de_baja_usuario(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)
