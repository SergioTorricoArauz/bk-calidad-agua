# analisis_muestreo/infrastructure/views/analisis_caudal_view.py

from rest_framework import viewsets, status
from rest_framework.response import Response

from analisis_muestreo.application.service.analisis_caudal_service_impl import AnalisisCaudalServiceImpl
from analisis_muestreo.infrastructure.repositories.analisis_caudal_repository_impl import AnalisisCaudalRepositoryImpl
from analisis_muestreo.infrastructure.serializers.analisis_caudal_serializer import AnalisisCaudalSerializer

repository = AnalisisCaudalRepositoryImpl()
service = AnalisisCaudalServiceImpl(repository)


class AnalisisCaudalViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        serializer = AnalisisCaudalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        analisis = service.crear_analisis(**serializer.validated_data)
        return Response(AnalisisCaudalSerializer(analisis).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(request, pk=None):
        analisis = service.obtener_analisis_por_id(int(pk))
        if not analisis:
            return Response({"detail": "Análisis no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(AnalisisCaudalSerializer(analisis).data)

    @staticmethod
    def list(request):
        salida_id = request.query_params.get('salida_id')
        if not salida_id:
            return Response({"detail": "Debe proporcionar el ID de la salida"}, status=status.HTTP_400_BAD_REQUEST)
        analisis_list = service.listar_analisis_por_salida(int(salida_id))
        return Response(AnalisisCaudalSerializer(analisis_list, many=True).data)

    @staticmethod
    def destroy(request, pk=None):
        service.eliminar_analisis(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def update(request, pk=None):
        serializer = AnalisisCaudalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        analisis = service.actualizar_analisis(int(pk), **serializer.validated_data)
        return Response(AnalisisCaudalSerializer(analisis).data)
    