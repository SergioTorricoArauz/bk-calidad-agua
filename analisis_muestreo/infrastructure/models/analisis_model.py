# analisis/infrastructure/models/analisis_model.py

from django.db import models
from salidas_de_campo.infrastructure.models.salida_de_campo_model import SalidaDeCampoModel


class AnalisisModel(models.Model):
    TIPO_ANALISIS_CHOICES = [
        ('turbidez', 'Turbidez'),
        ('caudal', 'Caudal'),
        ('ph', 'pH'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_ANALISIS_CHOICES)
    salida_de_campo = models.ForeignKey(SalidaDeCampoModel, on_delete=models.CASCADE, related_name="analisis")
    fecha = models.DateField(auto_now_add=True)
    datos = models.JSONField()  # Almacena datos específicos del análisis (e.g., turbidez, caudal)

    def __str__(self):
        return f"Analisis {self.tipo} para salida {self.salida_de_campo_id}"
