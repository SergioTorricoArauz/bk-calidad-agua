# usuarios/infrastructure/views/user_view.py
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response

from usuarios.application.permissions import IsAdmin, IsTechnician
from usuarios.application.services.user_service_impl import UserServiceImpl
from usuarios.infrastructure.serializers.user_serializer import UsuarioSerializer, UsuarioCrearSerializer

user_service = UserServiceImpl()


class UserViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        """
        Solo los administradores pueden crear usuarios.
        """
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

    def retrieve(self, request, pk=None):
        """
        Los técnicos y administradores pueden acceder al detalle de un usuario.
        """
        self.permission_classes = [IsTechnician | IsAdmin]
        self.check_permissions(request)

        try:
            user = user_service.obtener_usuario_por_id(int(pk))
            return Response(UsuarioSerializer(user).data)
        except ObjectDoesNotExist:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """
        Los técnicos y administradores pueden listar todos los usuarios.
        """
        self.permission_classes = [IsTechnician | IsAdmin]
        self.check_permissions(request)

        users = user_service.obtener_todos()
        return Response(UsuarioSerializer(users, many=True).data)

    @staticmethod
    def update(request, pk=None):
        """
        Solo los administradores pueden actualizar usuarios.
        """
        serializer = UsuarioSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = user_service.editar_usuario(int(pk), **serializer.validated_data)
            return Response(UsuarioSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk=None):
        """
        Solo los administradores pueden eliminar usuarios.
        """
        user_service.dar_de_baja_usuario(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)
