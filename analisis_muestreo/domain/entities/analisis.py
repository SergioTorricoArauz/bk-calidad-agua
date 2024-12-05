# analisis/domain/entities/analisis.py

from abc import ABC, abstractmethod
from datetime import date
from typing import Optional, Dict


class Analisis(ABC):
    def __init__(self, tipo: str, salida_de_campo_id: int, datos: Optional[Dict] = None,
                 fecha: Optional[date] = None, id: Optional[int] = None):
        self.id = id
        self.tipo = tipo
        self.salida_de_campo_id = salida_de_campo_id  # Relación con salida de campo
        self.fecha = fecha or date.today()
        self.datos = datos or {}  # Inicializa `datos` como un diccionario vacío si no se pasa

    @abstractmethod
    def validar(self):
        """Validaciones específicas para cada análisis."""
        pass

    @abstractmethod
    def detalles(self) -> dict:
        """Devuelve los detalles específicos del análisis."""
        pass

    def __str__(self):
        return f"Analisis(id={self.id}, tipo={self.tipo}, salida_de_campo_id={self.salida_de_campo_id}, fecha={self.fecha}, datos={self.datos})"
