# cuerpos_de_agua/infrastructure/models/cuerpo_de_agua_model.py

from django.db import models
from comunidades.infrastructure.models.comunidad_model import ComunidadModel


class CuerpoDeAguaModel(models.Model):
    TIPO_RIO = 1
    TIPO_ARROYO = 2
    TIPO_LAGO = 3
    TIPO_HUMEDAL = 4

    TIPOS_VALIDOS = [
        (TIPO_RIO, "Río"),
        (TIPO_ARROYO, "Arroyo"),
        (TIPO_LAGO, "Lago"),
        (TIPO_HUMEDAL, "Humedal")
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=TIPOS_VALIDOS)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    comunidad = models.ForeignKey(ComunidadModel, on_delete=models.CASCADE, related_name="cuerpos_de_agua")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
