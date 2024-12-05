# analisis/infrastructure/serializers/analisis_serializer.py

from rest_framework import serializers

from analisis_muestreo.domain.entities import AnalisisTurbidez, AnalisisCaudal, AnalisisPH
from analisis_muestreo.infrastructure.models import AnalisisModel


class AnalisisSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(choices=["turbidez", "caudal", "ph"])
    salida_de_campo_id = serializers.IntegerField()
    datos = serializers.JSONField()

    def create(self, validated_data):
        tipo = validated_data["tipo"]
        salida_de_campo_id = validated_data["salida_de_campo_id"]
        datos = validated_data["datos"]

        # Crear el análisis dinámicamente basado en el tipo
        if tipo == "turbidez":
            analisis = AnalisisTurbidez(turbidez=datos["turbidez"], salida_de_campo_id=salida_de_campo_id)
        elif tipo == "caudal":
            analisis = AnalisisCaudal(
                velocidad=datos["velocidad"],
                ancho=datos["ancho"],
                profundidad_media=datos["profundidad_media"],
                salida_de_campo_id=salida_de_campo_id,
            )
        elif tipo == "ph":
            analisis = AnalisisPH(ph=datos["ph"], salida_de_campo_id=salida_de_campo_id)
        else:
            raise serializers.ValidationError("Tipo de análisis no soportado")

        # Usamos el servicio para guardar el análisis
        analisis_service = self.context["analisis_service"]
        return analisis_service.registrar_analisis(tipo, salida_de_campo_id, datos)


class AnalisisDetailSerializer(serializers.ModelSerializer):
    salida_de_campo = serializers.IntegerField(source='salida_de_campo_id')  # Ajusta el campo al atributo correcto

    class Meta:
        model = AnalisisModel
        fields = ['id', 'tipo', 'salida_de_campo', 'fecha', 'datos']
