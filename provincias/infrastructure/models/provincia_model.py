# provincias/infrastructure/models/provincia_model.py

from django.db import models
from departamentos.infrastructure.models import DepartamentoModel


class ProvinciaModel(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    departamento = models.ForeignKey(DepartamentoModel, on_delete=models.CASCADE, related_name="provincias")

    def __str__(self):
        return self.nombre
