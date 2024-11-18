# salidas_de_campo/infrastructure/views/salida_de_campo_view.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from salidas_de_campo.application.services.salida_de_campo_service_impl import SalidaDeCampoServiceImpl
from salidas_de_campo.infrastructure.repositories.salida_de_campo_repository_impl import SalidaDeCampoRepositoryImpl
from salidas_de_campo.infrastructure.serializers.salida_de_campo_serializer import SalidaDeCampoSerializer

# Configuración del servicio y repositorio
salida_de_campo_repository = SalidaDeCampoRepositoryImpl()
salida_de_campo_service = SalidaDeCampoServiceImpl(salida_de_campo_repository)


class SalidaDeCampoViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        salidas = salida_de_campo_service.listar_salidas()
        serializer = SalidaDeCampoSerializer(salidas, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request):
        serializer = SalidaDeCampoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        salida = salida_de_campo_service.crear_salida(
            fecha_inicio=serializer.validated_data['fecha_inicio'],
            fecha_fin=serializer.validated_data['fecha_fin'],
            descripcion=serializer.validated_data['descripcion'],
            tecnicos_asignados=serializer.validated_data['tecnicos_asignados'],
            cuerpos_de_agua_asignados=serializer.validated_data['cuerpos_de_agua_asignados']
        )
        return Response(SalidaDeCampoSerializer(salida).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(request, pk=None):
        salida = salida_de_campo_service.obtener_salida_por_id(int(pk))
        if salida is None:
            return Response({"detail": "Salida de campo no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SalidaDeCampoSerializer(salida)
        return Response(serializer.data)

    @staticmethod
    def update(request, pk=None):
        serializer = SalidaDeCampoSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        salida = salida_de_campo_service.editar_salida(
            id=int(pk),
            fecha_inicio=serializer.validated_data.get('fecha_inicio'),
            fecha_fin=serializer.validated_data.get('fecha_fin'),
            descripcion=serializer.validated_data.get('descripcion'),
            tecnicos_asignados=serializer.validated_data.get('tecnicos_asignados'),  # Lista de IDs de técnicos
            cuerpos_de_agua_asignados=serializer.validated_data.get('cuerpos_de_agua_asignados')
            # Lista de IDs de cuerpos de agua
        )
        return Response(SalidaDeCampoSerializer(salida).data, status=status.HTTP_200_OK)

    @staticmethod
    def destroy(request, pk=None):
        salida_de_campo_service.eliminar_salida(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)
