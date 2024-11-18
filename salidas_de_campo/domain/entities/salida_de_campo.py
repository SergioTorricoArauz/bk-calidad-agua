# salidas_de_campo/domain/entities/salida_de_campo.py

from typing import List, Optional
from datetime import date

from salidas_de_campo.domain.exceptions import SalidaDeCampoException


class SalidaDeCampo:
    def __init__(self, fecha_inicio: date, fecha_fin: date, descripcion: str,
                 tecnicos_asignados: Optional[List[int]] = None,  # IDs de User
                 cuerpos_de_agua_asignados: Optional[List[int]] = None,  # IDs de CuerpoDeAgua
                 id: Optional[int] = None):
        if fecha_inicio > fecha_fin:
            raise SalidaDeCampoException("La fecha de inicio no puede ser posterior a la fecha de fin.")
        if not descripcion:
            raise SalidaDeCampoException("La descripción es obligatoria.")

        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.descripcion = descripcion
        self.tecnicos_asignados = tecnicos_asignados or []
        self.cuerpos_de_agua_asignados = cuerpos_de_agua_asignados or []

    def __str__(self):
        return f"SalidaDeCampo(id={self.id}, fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin}, descripcion={self.descripcion})"
