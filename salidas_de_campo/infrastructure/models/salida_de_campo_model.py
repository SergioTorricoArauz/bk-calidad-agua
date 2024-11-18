# salidas_de_campo/infrastructure/models/salida_de_campo_model.py

from django.db import models
from django.contrib.auth.models import User
from cuerpos_de_agua.infrastructure.models.cuerpo_de_agua_model import CuerpoDeAguaModel


class SalidaDeCampoModel(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    tecnicos_asignados = models.ManyToManyField(User, related_name="salidas_de_campo")
    cuerpos_de_agua_asignados = models.ManyToManyField(CuerpoDeAguaModel, related_name="salidas_de_campo")

    def __str__(self):
        return f"Salida de Campo ({self.fecha_inicio} - {self.fecha_fin}): {self.descripcion[:30]}"
