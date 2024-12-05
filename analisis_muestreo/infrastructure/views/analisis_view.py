# analisis/infrastructure/views/analisis_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from analisis_muestreo.application.service import AnalisisServiceImpl
from analisis_muestreo.infrastructure.serializers.analisis_serializer import AnalisisSerializer, \
    AnalisisDetailSerializer
from analisis_muestreo.infrastructure.repositories.analisis_repository_impl import AnalisisRepositoryImpl
from salidas_de_campo.infrastructure.models import SalidaDeCampoModel


class AnalisisView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        user = request.user

        # Validar que el usuario es técnico
        if not user.groups.filter(name='Tecnico').exists():
            return Response(
                {"error": "Solo los técnicos pueden registrar análisis."},
                status=status.HTTP_403_FORBIDDEN
            )

        salida_de_campo_id = request.data.get("salida_de_campo_id")

        # Validar relación técnico-salida
        if not SalidaDeCampoModel.objects.filter(
                id=salida_de_campo_id,
                tecnicos_asignados__id=user.id
        ).exists():
            return Response(
                {"error": "No tiene permiso para registrar análisis en esta salida de campo."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Crear análisis
        serializer = AnalisisSerializer(
            data=request.data,
            context={"analisis_service": AnalisisServiceImpl(AnalisisRepositoryImpl())}
        )
        if serializer.is_valid():
            analisis = serializer.save()
            return Response({"id": analisis.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, *args, **kwargs):
        user = request.user

        if user.groups.filter(name='Administrador').exists():
            # Administrador puede ver todos los análisis
            analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
            analisis_list = analisis_service.listar_todos()
        elif user.groups.filter(name='Tecnico').exists():
            # Técnico ve solo análisis de sus salidas de campo
            salidas_ids = list(SalidaDeCampoModel.objects.filter(
                tecnicos_asignados__id=user.id
            ).values_list('id', flat=True))

            analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
            analisis_list = analisis_service.listar_analisis_por_salidas(salidas_ids)
        else:
            return Response(
                {"error": "No tiene permiso para ver los análisis."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = AnalisisDetailSerializer(analisis_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnalisisDetailView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        """
        Obtener el detalle de un análisis.
        """
        user = request.user
        analisis_id = kwargs.get("id")

        if not analisis_id:
            return Response({"error": "El parámetro id es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

        analisis_service = AnalisisServiceImpl(AnalisisRepositoryImpl())
        analisis = analisis_service.obtener_analisis_por_id(int(analisis_id))

        if not analisis:
            return Response({"error": "Análisis no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Validar acceso para técnicos
        if user.groups.filter(name='Técnico').exists():
            if not SalidaDeCampoModel.objects.filter(
                    id=analisis.salida_de_campo_id,
                    tecnicos_asignados__id=user.id
            ).exists():
                return Response(
                    {"error": "No tiene permiso para ver este análisis."},
                    status=status.HTTP_403_FORBIDDEN
                )

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
