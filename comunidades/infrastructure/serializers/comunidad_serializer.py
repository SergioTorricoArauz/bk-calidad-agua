# comunidades/infrastructure/serializers/comunidad_serializer.py

from rest_framework import serializers
from comunidades.infrastructure.models.comunidad_model import ComunidadModel


class ComunidadSerializer(serializers.ModelSerializer):
    provincia_id = serializers.IntegerField()

    class Meta:
        model = ComunidadModel
        fields = ['id', 'nombre', 'provincia_id']
