# provincias/infrastructure/views/provincia_view.py
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

from comunidades.infrastructure.serializers import ComunidadSerializer
from provincias.infrastructure.serializers.provincia_serializer import ProvinciaSerializer
from provincias.application.services.provincia_service_impl import ProvinciaServiceImpl
from provincias.infrastructure.repositories.provincia_repository_impl import ProvinciaRepositoryImpl

provincia_repository = ProvinciaRepositoryImpl()
provincia_service = ProvinciaServiceImpl(provincia_repository)


class ProvinciaViewSet(viewsets.ViewSet):

    @staticmethod
    def list(request):
        provincias = provincia_service.listar_provincias()
        serializer = ProvinciaSerializer(provincias, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request):
        serializer = ProvinciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        provincia = provincia_service.crear_provincia(
            nombre=serializer.validated_data['nombre'],
            departamento_id=serializer.validated_data['departamento_id']
        )
        return Response(ProvinciaSerializer(provincia).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(request, pk=None):
        provincia = provincia_service.obtener_provincia_por_id(int(pk))
        serializer = ProvinciaSerializer(provincia)
        return Response(serializer.data)

    @staticmethod
    def destroy(request, pk=None):
        provincia_service.eliminar_provincia(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def update(request, pk=None):
        serializer = ProvinciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provincia = provincia_service.actualizar_provincia(
            id=int(pk),
            nombre=serializer.validated_data['nombre'],
            departamento_id=serializer.validated_data['departamento_id']
        )
        return Response(ProvinciaSerializer(provincia).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='comunidades')
    def listar_comunidades(self, request, pk=None):
        comunidades = provincia_service.listar_comunidades(int(pk))
        serializer = ComunidadSerializer(comunidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
