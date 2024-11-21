# analisis_muestreo/infrastructure/serializers/analisis_turbidez_serializer.py

from rest_framework import serializers
from analisis_muestreo.infrastructure.models.analisis_turbidez_model import AnalisisTurbidezModel


class AnalisisTurbidezSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalisisTurbidezModel
        fields = ['id', 'ntu', 'fecha', 'tecnico_id', 'salida_id']
