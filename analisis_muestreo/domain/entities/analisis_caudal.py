# analisis_muestreo/domain/entities/analisis_caudal.py
from datetime import datetime
from typing import Optional
from analisis_muestreo.domain.exception import AnalisisMuestreoException


class AnalisisCaudal:
    def __init__(self, velocidad: float, ancho: float, profundidad_media: float,
                 fecha: datetime, tecnico_id: int, salida_id: int, id: Optional[int] = None):
        if velocidad <= 0 or ancho <= 0 or profundidad_media <= 0:
            raise AnalisisMuestreoException("Los valores de velocidad, ancho y profundidad deben ser positivos.")
        self.id = id
        self.velocidad = velocidad
        self.ancho = ancho
        self.profundidad_media = profundidad_media
        self.fecha = fecha
        self.tecnico_id = tecnico_id
        self.salida_id = salida_id

    def calcular_caudal(self) -> float:
        return self.ancho * self.profundidad_media * self.velocidad

    def __str__(self):
        return (f"Análisis de Caudal (Velocidad: {self.velocidad} m/s, Ancho: {self.ancho} m, "
                f"Profundidad Media: {self.profundidad_media} m, Fecha: {self.fecha}, Técnico ID: {self.tecnico_id}, "
                f"Salida ID: {self.salida_id}, Caudal: {self.calcular_caudal()} m³/s)")
