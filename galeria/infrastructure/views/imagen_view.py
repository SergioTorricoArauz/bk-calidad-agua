# galeria/infrastructure/views/imagen_view.py
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, status
from rest_framework.response import Response
from galeria.application.services.imagen_service_impl import ImagenServiceImpl
from galeria.infrastructure.helpers import ContentTypeHelper
from galeria.infrastructure.models import ImagenModel
from galeria.infrastructure.repositories.imagen_repository_impl import ImagenRepositoryImpl
from galeria.infrastructure.serializers.imagen_serializer import ImagenSerializer

imagen_repository = ImagenRepositoryImpl()
imagen_service = ImagenServiceImpl(imagen_repository)


class ImagenViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        relacionado_tipo = request.query_params.get('relacionado_tipo')
        relacionado_id = request.query_params.get('relacionado_id')

        if not relacionado_tipo or not relacionado_id:
            return Response({"error": "Debe proporcionar 'relacionado_tipo' y 'relacionado_id'."},
                            status=status.HTTP_400_BAD_REQUEST)

        imagenes = imagen_service.listar_imagenes_por_relacion(relacionado_tipo, int(relacionado_id))
        serializer = ImagenSerializer(imagenes, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ImagenSerializer(data=request.data)
        if serializer.is_valid():
            relacionado_tipo_str = serializer.validated_data['relacionado_tipo'].lower()  # Convertir a minúsculas
            relacionado_id = serializer.validated_data['relacionado_id']

            # Obtener app_label y model_name del mapping
            app_label, model_name = self._get_app_label(relacionado_tipo_str)
            if not app_label or not model_name:
                return Response(
                    {"error": f"Tipo relacionado inválido: {relacionado_tipo_str}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                # Obtener el ContentType basado en app_label y model_name
                content_type = ContentType.objects.get(app_label=app_label, model=model_name)
            except ContentType.DoesNotExist:
                return Response(
                    {"error": f"ContentType no encontrado para {relacionado_tipo_str}."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Obtener el modelo relacionado y validar que el objeto existe
            relacionado_model = content_type.model_class()
            try:
                relacionado_obj = relacionado_model.objects.get(id=relacionado_id)
            except relacionado_model.DoesNotExist:
                return Response(
                    {"error": f"No se encontró el objeto relacionado con ID {relacionado_id}."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Crear la imagen en la base de datos
            try:
                imagen = ImagenModel.objects.create(
                    url=serializer.validated_data['url'],
                    relacionado_tipo=content_type,
                    relacionado_id=relacionado_obj.id
                )
            except Exception as e:
                return Response(
                    {"error": f"Error al crear la imagen: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Retornar la respuesta con los datos de la imagen creada
            return Response(ImagenSerializer(imagen).data, status=status.HTTP_201_CREATED)

        # Si el serializer no es válido, retornar errores de validación
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        imagen = imagen_service.obtener_imagen_por_id(int(pk))
        if imagen is None:
            return Response({"error": "Imagen no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ImagenSerializer(imagen).data)

    @staticmethod
    def destroy(request, pk=None):
        imagen_service.eliminar_imagen(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def _get_app_label(relacionado_tipo_str):
        # Mapeo de tipos relacionados a (app_label, model_name)
        mapping = {
            'salidadecampo': ('salidas_de_campo', 'salidadecampomodel'),
            'analisiscaudal': ('analisis_muestreo', 'analisicaudalmodel'),
            'analisisturbidez': ('analisis_muestreo', 'analisisturbidezmodel'),
        }
        relacionado_tipo_str = relacionado_tipo_str.lower()
        if relacionado_tipo_str not in mapping:
            return None, None
        return mapping[relacionado_tipo_str]
