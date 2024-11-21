# galeria/infrastructure/serializers/imagen_serializer.py

from rest_framework import serializers
from galeria.infrastructure.models.imagen_model import ImagenModel


class ImagenSerializer(serializers.ModelSerializer):
    relacionado_tipo = serializers.CharField()  # Aceptar string
    relacionado_id = serializers.IntegerField()

    class Meta:
        model = ImagenModel
        fields = ['id', 'url', 'relacionado_tipo', 'relacionado_id']
