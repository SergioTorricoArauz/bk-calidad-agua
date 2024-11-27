# departamentos/infrastructure/views/departamento_view.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from departamentos.application.services import DepartamentoServiceImpl
from departamentos.domain.exception import DepartamentoError
from departamentos.infrastructure.repositories import DepartamentoRepositoryImpl
from departamentos.infrastructure.serializers import DepartamentoSerializer
from provincias.infrastructure.serializers import ProvinciaSerializer
from usuarios.application.permissions import IsAdmin

# Configuramos el repositorio y el servicio
departamento_repository = DepartamentoRepositoryImpl()
departamento_service = DepartamentoServiceImpl(departamento_repository)


class DepartamentoViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    @staticmethod
    def list(request):
        departamentos = departamento_service.listar_departamentos()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request):
        serializer = DepartamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        departamento = departamento_service.crear_departamento(serializer.validated_data['nombre'])
        return Response(DepartamentoSerializer(departamento).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def update(request, pk=None):
        serializer = DepartamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            departamento = departamento_service.actualizar_departamento(int(pk), serializer.validated_data['nombre'])
            return Response(DepartamentoSerializer(departamento).data, status=status.HTTP_200_OK)
        except DepartamentoError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def retrieve(request, pk=None):
        try:
            departamento = departamento_service.obtener_departamento_por_id(int(pk))
            serializer = DepartamentoSerializer(departamento)
            return Response(serializer.data)
        except DepartamentoError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def destroy(request, pk=None):
        try:
            departamento_service.eliminar_departamento_por_id(int(pk))
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DepartamentoError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='provincias')
    def listar_provincias(self, request, pk=None):
        provincias = departamento_service.listar_provincias(int(pk))
        serializer = ProvinciaSerializer(provincias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
