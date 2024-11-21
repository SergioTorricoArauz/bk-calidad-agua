# analisis_muestreo/infrastructure/serializers/analisis_caudal_serializer.py

from rest_framework import serializers
from analisis_muestreo.infrastructure.models.analisis_caudal_model import AnalisisCaudalModel


class AnalisisCaudalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalisisCaudalModel
        fields = ['id', 'velocidad', 'ancho', 'profundidad_media', 'fecha', 'tecnico_id', 'salida_id']
