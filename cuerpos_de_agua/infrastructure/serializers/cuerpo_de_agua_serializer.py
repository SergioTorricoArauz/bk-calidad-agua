# cuerpos_de_agua/infrastructure/serializers/cuerpo_de_agua_serializer.py

from rest_framework import serializers
from cuerpos_de_agua.infrastructure.models.cuerpo_de_agua_model import CuerpoDeAguaModel


class CuerpoDeAguaSerializer(serializers.ModelSerializer):
    comunidad_id = serializers.IntegerField()

    class Meta:
        model = CuerpoDeAguaModel
        fields = ['id', 'nombre', 'tipo', 'latitud', 'longitud', 'comunidad_id']
