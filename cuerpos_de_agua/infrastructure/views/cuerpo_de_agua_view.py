# cuerpos_de_agua/infrastructure/views/cuerpo_de_agua_view.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from cuerpos_de_agua.application.services.cuerpo_de_agua_service_impl import CuerpoDeAguaServiceImpl
from cuerpos_de_agua.infrastructure.repositories.cuerpo_de_agua_repository_impl import CuerpoDeAguaRepositoryImpl
from cuerpos_de_agua.infrastructure.serializers.cuerpo_de_agua_serializer import CuerpoDeAguaSerializer
from usuarios.application.permissions import IsAdmin

cuerpo_de_agua_repository = CuerpoDeAguaRepositoryImpl()
cuerpo_de_agua_service = CuerpoDeAguaServiceImpl(cuerpo_de_agua_repository)


class CuerpoDeAguaViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    @staticmethod
    def create(request):
        serializer = CuerpoDeAguaSerializer(data=request.data)
        if serializer.is_valid():
            comunidad_id = serializer.validated_data.get("comunidad_id")

            cuerpo_de_agua = cuerpo_de_agua_service.crear_cuerpo_de_agua(
                serializer.validated_data.get("nombre"),
                serializer.validated_data.get("tipo"),
                serializer.validated_data.get("latitud"),
                serializer.validated_data.get("longitud"),
                comunidad_id
            )
            return Response(CuerpoDeAguaSerializer(cuerpo_de_agua).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        cuerpo_de_agua = cuerpo_de_agua_service.obtener_cuerpo_de_agua_por_id(int(pk))
        if cuerpo_de_agua is None:
            return Response({"error": "Cuerpo de agua no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CuerpoDeAguaSerializer(cuerpo_de_agua)
        return Response(serializer.data)

    @staticmethod
    def list(request):
        cuerpos_de_agua = cuerpo_de_agua_service.listar_cuerpos_de_agua()
        serializer = CuerpoDeAguaSerializer(cuerpos_de_agua, many=True)
        return Response(serializer.data)

    @staticmethod
    def destroy(request, pk=None):
        try:
            cuerpo_de_agua_service.eliminar_cuerpo_de_agua(int(pk))
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request, pk=None):
        serializer = CuerpoDeAguaSerializer(data=request.data)
        if serializer.is_valid():
            cuerpo_de_agua = cuerpo_de_agua_service.obtener_cuerpo_de_agua_por_id(int(pk))
            if cuerpo_de_agua is None:
                return Response({"error": "Cuerpo de agua no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            cuerpo_de_agua.nombre = serializer.validated_data.get("nombre")
            cuerpo_de_agua.tipo = serializer.validated_data.get("tipo")
            cuerpo_de_agua.latitud = serializer.validated_data.get("latitud")
            cuerpo_de_agua.longitud = serializer.validated_data.get("longitud")
            cuerpo_de_agua.comunidad_id = serializer.validated_data.get("comunidad_id")
            cuerpo_de_agua_service.actualizar_cuerpo_de_agua(cuerpo_de_agua)
            return Response(CuerpoDeAguaSerializer(cuerpo_de_agua).data, status=status.HTTP_200_OK)
