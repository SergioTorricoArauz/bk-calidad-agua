from rest_framework import serializers
from salidas_de_campo.infrastructure.models.salida_de_campo_model import SalidaDeCampoModel


class SalidaDeCampoSerializer(serializers.ModelSerializer):
    tecnicos_asignados = serializers.ListField(child=serializers.IntegerField())
    cuerpos_de_agua_asignados = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = SalidaDeCampoModel
        fields = ['id', 'fecha_inicio', 'fecha_fin', 'descripcion', 'tecnicos_asignados', 'cuerpos_de_agua_asignados']
