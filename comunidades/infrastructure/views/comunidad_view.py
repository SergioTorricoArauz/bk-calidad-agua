# comunidades/infrastructure/views/comunidad_view.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from comunidades.application.services.comunidad_service_impl import ComunidadServiceImpl
from comunidades.domain.exception import ComunidadException
from comunidades.infrastructure.repositories.comunidad_repository_impl import ComunidadRepositoryImpl
from comunidades.infrastructure.serializers.comunidad_serializer import ComunidadSerializer
from cuerpos_de_agua.domain.ports.input import cuerpo_de_agua_service
from cuerpos_de_agua.infrastructure.serializers import CuerpoDeAguaSerializer

comunidad_repository = ComunidadRepositoryImpl()
comunidad_service = ComunidadServiceImpl(comunidad_repository)


class ComunidadViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        comunidades = comunidad_service.listar_comunidades()
        serializer = ComunidadSerializer(comunidades, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request):
        serializer = ComunidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nombre = serializer.validated_data['nombre']
        provincia_id = serializer.validated_data['provincia_id']

        comunidad = comunidad_service.crear_comunidad(nombre=nombre, provincia_id=provincia_id)
        return Response(ComunidadSerializer(comunidad).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(request, pk=None):
        comunidad = comunidad_service.obtener_comunidad_por_id(int(pk))
        if comunidad is None:
            return Response({"error": "Comunidad no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComunidadSerializer(comunidad)
        return Response(serializer.data)

    @staticmethod
    def destroy(request, pk=None):
        try:
            comunidad_service.eliminar_comunidad(int(pk))
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request, pk=None):
        serializer = ComunidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nombre = serializer.validated_data['nombre']
        provincia_id = serializer.validated_data['provincia_id']

        try:
            comunidad = comunidad_service.actualizar_comunidad(id=int(pk), nombre=nombre, provincia_id=provincia_id)
            return Response(ComunidadSerializer(comunidad).data, status=status.HTTP_200_OK)
        except ComunidadException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='cuerpos_de_agua')
    def listar_cuerpos_de_agua(self, request, pk=None):
        """Listar cuerpos de agua para una comunidad específica."""
        if pk is None:
            return Response({"error": "ID de la comunidad no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Llama al servicio de cuerpos de agua para obtener la lista por comunidad
            cuerpos_de_agua = cuerpo_de_agua_service.listar_cuerpos_de_agua_por_comunidad(int(pk))
            serializer = CuerpoDeAguaSerializer(cuerpos_de_agua, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
