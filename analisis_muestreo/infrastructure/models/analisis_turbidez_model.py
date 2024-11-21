# analisis_muestreo/infrastructure/models/analisis_turbidez_model.py

from django.db import models

class AnalisisTurbidezModel(models.Model):
    ntu = models.FloatField()
    fecha = models.DateTimeField()
    tecnico_id = models.IntegerField()
    salida_id = models.IntegerField()

    def __str__(self):
        return f"Análisis de Turbidez (ID: {self.id}, NTU: {self.ntu}, Fecha: {self.fecha})"
