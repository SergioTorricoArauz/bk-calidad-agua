# analisis/infrastructure/views/analisis_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from analisis_muestreo.application.service import AnalisisServiceImpl
from analisis_muestreo.infrastructure.serializers.analisis_serializer import AnalisisSerializer, \
    AnalisisDetailSerializer
from analisis_muestreo.infrastructure.repositories.analisis_repository_impl import AnalisisRepositoryImpl


class AnalisisView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        """
        Crear un nuevo análisis.
        """
        serializer = AnalisisSerializer(data=request.data,
                                        context={"analisis_service": AnalisisServiceImpl(AnalisisRepositoryImpl())})
        if serializer.is_valid():
            analisis = serializer.save()
            return Response({"id": analisis.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, *args, **kwargs):
        """
        Listar todos los análisis asociados a una salida de campo.
        """
        salida_de_campo_id = request.query_params.get('salida_de_campo_id')
        if not salida_de_campo_id:
            return Response({"error": "El parámetro salida_de_campo_id es obligatorio."},
                            status=status.HTTP_400_BAD_REQUEST)

        analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
        analisis_list = analisis_service.listar_analisis_por_salida(salida_de_campo_id=int(salida_de_campo_id))

        serializer = AnalisisDetailSerializer(analisis_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnalisisDetailView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        """
        Obtener el detalle de un análisis por su ID.
        """
        analisis_id = kwargs.get('id')
        if not analisis_id:
            return Response({"error": "El parámetro id es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

        analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
        analisis = analisis_service.obtener_analisis_por_id(int(analisis_id))

        if analisis is None:
            return Response({"error": "Análisis no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnalisisDetailSerializer(analisis)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, *args, **kwargs):
        """
        Eliminar un análisis por su ID.
        """
        analisis_id = kwargs.get('id')
        if not analisis_id:
            return Response({"error": "El parámetro id es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

        analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
        try:
            analisis_service.eliminar_analisis(int(analisis_id))
            return Response({"message": "Análisis eliminado exitosamente."}, status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
