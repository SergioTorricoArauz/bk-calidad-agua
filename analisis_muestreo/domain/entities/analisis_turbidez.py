# analisis_muestreo/domain/entities/analisis_turbidez.py


from datetime import datetime
from typing import Optional
from analisis_muestreo.domain.exception import AnalisisMuestreoException


class AnalisisTurbidez:
    def __init__(self, ntu: float, fecha: datetime, tecnico_id: int, salida_id: int, id: Optional[int] = None):
        if ntu < 0:
            raise AnalisisMuestreoException("El valor de NTU no puede ser negativo.")
        self.id = id
        self.ntu = ntu
        self.fecha = fecha
        self.tecnico_id = tecnico_id
        self.salida_id = salida_id

    def clasificar_turbidez(self) -> str:
        if self.ntu < 1:
            return "Agua muy clara, casi cristalina."
        elif self.ntu <= 5:
            return "Agua clara, ideal para consumo humano."
        elif self.ntu <= 10:
            return "Agua ligeramente turbia."
        elif self.ntu <= 50:
            return "Agua turbia."
        else:
            return "Agua muy turbia."

    def __str__(self):
        return (f"Análisis de Turbidez (NTU: {self.ntu}, Fecha: {self.fecha}, Técnico ID: {self.tecnico_id}, "
                f"Salida ID: {self.salida_id}): {self.clasificar_turbidez()}")
