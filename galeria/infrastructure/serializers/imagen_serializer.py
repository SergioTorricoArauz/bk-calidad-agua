# galeria/infrastructure/serializers/imagen_serializer.py

from rest_framework import serializers
from galeria.infrastructure.models.imagen_model import ImagenModel


class ImagenSerializer(serializers.ModelSerializer):
    relacionado_tipo = serializers.CharField()
    relacionado_id = serializers.IntegerField()

    class Meta:
        model = ImagenModel
        fields = ['id', 'url', 'relacionado_tipo', 'relacionado_id']
