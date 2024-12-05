from datetime import date
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from salidas_de_campo.application.services.salida_de_campo_service_impl import SalidaDeCampoServiceImpl
from salidas_de_campo.domain.exceptions import SalidaDeCampoException
from salidas_de_campo.infrastructure.repositories.salida_de_campo_repository_impl import SalidaDeCampoRepositoryImpl
from salidas_de_campo.infrastructure.serializers.salida_de_campo_serializer import SalidaDeCampoSerializer
from usuarios.application.permissions import IsAdmin

salida_de_campo_repository = SalidaDeCampoRepositoryImpl()
salida_de_campo_service = SalidaDeCampoServiceImpl(salida_de_campo_repository)


class SalidaDeCampoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return super().get_permissions()

    @staticmethod
    def list(request):
        user = request.user

        try:
            # Determinar el técnico ID según el rol del usuario
            if user.groups.filter(name='Administrador').exists():
                tecnico_id = request.query_params.get("tecnico_id")
            elif user.groups.filter(name='Tecnico').exists():
                tecnico_id = user.id
            else:
                return Response(
                    {"detail": "No tiene permiso para acceder a esta vista."},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Validar filtros de fecha
            fecha_inicio = request.query_params.get("fecha_inicio")
            fecha_fin = request.query_params.get("fecha_fin")

            salidas = salida_de_campo_service.filtrar_salidas(
                tecnico_id=int(tecnico_id) if tecnico_id else None,
                fecha_inicio=date.fromisoformat(fecha_inicio) if fecha_inicio else None,
                fecha_fin=date.fromisoformat(fecha_fin) if fecha_fin else None,
            )
        except (ValueError, TypeError, SalidaDeCampoException) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialización y respuesta
        serializer = SalidaDeCampoSerializer(salidas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def create(request):
        serializer = SalidaDeCampoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            salida = salida_de_campo_service.crear_salida(
                fecha_inicio=serializer.validated_data['fecha_inicio'],
                fecha_fin=serializer.validated_data['fecha_fin'],
                descripcion=serializer.validated_data['descripcion'],
                tecnicos_asignados=serializer.validated_data['tecnicos_asignados'],
                cuerpos_de_agua_asignados=serializer.validated_data['cuerpos_de_agua_asignados']
            )
            return Response(SalidaDeCampoSerializer(salida).data, status=status.HTTP_201_CREATED)
        except SalidaDeCampoException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        user = request.user

        try:
            salida = salida_de_campo_service.obtener_salida_por_id(int(pk))
            if not user.groups.filter(name='Administrador').exists() and user.id not in salida.tecnicos_asignados:
                return Response(
                    {"detail": "No tiene permiso para acceder a esta salida de campo."},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer = SalidaDeCampoSerializer(salida)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SalidaDeCampoException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def update(request, pk=None):
        serializer = SalidaDeCampoSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            salida = salida_de_campo_service.editar_salida(
                id=int(pk),
                fecha_inicio=serializer.validated_data.get('fecha_inicio'),
                fecha_fin=serializer.validated_data.get('fecha_fin'),
                descripcion=serializer.validated_data.get('descripcion'),
                tecnicos_asignados=serializer.validated_data.get('tecnicos_asignados'),
                cuerpos_de_agua_asignados=serializer.validated_data.get('cuerpos_de_agua_asignados')
            )
            return Response(SalidaDeCampoSerializer(salida).data, status=status.HTTP_200_OK)
        except SalidaDeCampoException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk=None):
        try:
            salida_de_campo_service.eliminar_salida(int(pk))
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SalidaDeCampoException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
