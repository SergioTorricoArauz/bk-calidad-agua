# analisis_muestreo/infrastructure/models/analisis_caudal_model.py

from django.db import models

class AnalisisCaudalModel(models.Model):
    velocidad = models.FloatField()
    ancho = models.FloatField()
    profundidad_media = models.FloatField()
    fecha = models.DateTimeField()
    tecnico_id = models.IntegerField()
    salida_id = models.IntegerField()

    def __str__(self):
        return f"Análisis de Caudal (ID: {self.id}, Velocidad: {self.velocidad}, Caudal Calculado: {self.velocidad * self.ancho * self.profundidad_media})"
