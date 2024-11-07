# departamentos/infrastructure/models/departamento_model.py

from django.db import models


class DepartamentoModel(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
