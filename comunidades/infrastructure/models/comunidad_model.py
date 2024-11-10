# comunidades/infrastructure/models/comunidad_model.py

from django.db import models
from provincias.infrastructure.models import ProvinciaModel


class ComunidadModel(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(ProvinciaModel, on_delete=models.CASCADE, related_name="comunidades")

    def __str__(self):
        return self.nombre
