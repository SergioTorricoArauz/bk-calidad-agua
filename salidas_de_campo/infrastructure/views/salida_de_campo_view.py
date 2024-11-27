# salidas_de_campo/infrastructure/views/salida_de_campo_view.py
from datetime import date

from rest_framework import viewsets, status
from rest_framework.response import Response
from salidas_de_campo.application.services.salida_de_campo_service_impl import SalidaDeCampoServiceImpl
from salidas_de_campo.infrastructure.repositories.salida_de_campo_repository_impl import SalidaDeCampoRepositoryImpl
from salidas_de_campo.infrastructure.serializers.salida_de_campo_serializer import SalidaDeCampoSerializer
from usuarios.application.permissions import IsAdmin

salida_de_campo_repository = SalidaDeCampoRepositoryImpl()
salida_de_campo_service = SalidaDeCampoServiceImpl(salida_de_campo_repository)


class SalidaDeCampoViewSet(viewsets.ViewSet):

    @staticmethod
    def list(request):
        user = request.user

        if user.groups.filter(name='Administrador').exists():
            tecnico_id = request.query_params.get("tecnico_id")
        elif user.groups.filter(name='Tecnico').exists():
            tecnico_id = user.id  # Solo ve sus propias salidas
        else:
            return Response(
                {"detail": "No tiene permiso para acceder a esta vista."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Parámetros de filtrado opcionales
        fecha_inicio = request.query_params.get("fecha_inicio")
        fecha_fin = request.query_params.get("fecha_fin")

        try:
            salidas = salida_de_campo_service.filtrar_salidas(
                tecnico_id=int(tecnico_id) if tecnico_id else None,
                fecha_inicio=date.fromisoformat(fecha_inicio) if fecha_inicio else None,
                fecha_fin=date.fromisoformat(fecha_fin) if fecha_fin else None,
            )
        except ValueError:
            return Response({"error": "Los parámetros de filtro no son válidos."}, status=status.HTTP_400_BAD_REQUEST)

        # Serialización y respuesta
        serializer = SalidaDeCampoSerializer(salidas, many=True)
        return Response(serializer.data)

    def create(self, request):
        self.permission_classes = [IsAdmin]
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
        user = request.user

        salida = salida_de_campo_service.obtener_salida_por_id(int(pk))
        if not salida:
            return Response({"detail": "Salida de campo no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        if not user.groups.filter(name='Administrador').exists() and user.id not in salida.tecnicos_asignados:
            return Response(
                {"detail": "No tiene permiso para acceder a esta salida."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = SalidaDeCampoSerializer(salida)
        return Response(serializer.data)

    def update(self, request, pk=None):
        self.permission_classes = [IsAdmin]
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

    def destroy(self, request, pk=None):
        self.permission_classes = [IsAdmin]
        salida_de_campo_service.eliminar_salida(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)
