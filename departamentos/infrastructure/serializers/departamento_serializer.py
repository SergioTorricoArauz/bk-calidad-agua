# departamentos/infrastructure/serializers/departamento_serializer.py

from rest_framework import serializers

from departamentos.infrastructure.models import DepartamentoModel


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoModel
        fields = ['id', 'nombre']
