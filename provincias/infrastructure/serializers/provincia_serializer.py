# provincias/infrastructure/serializers/provincia_serializer.py

from rest_framework import serializers
from provincias.infrastructure.models.provincia_model import ProvinciaModel


class ProvinciaSerializer(serializers.ModelSerializer):
    departamento_id = serializers.IntegerField()

    class Meta:
        model = ProvinciaModel
        fields = ['id', 'nombre', 'departamento_id']
