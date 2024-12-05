# salidas_de_campo/domain/entities/salida_de_campo.py

from typing import List, Optional
from datetime import date

from salidas_de_campo.domain.exceptions import SalidaDeCampoException


class SalidaDeCampo:
    def __init__(self, fecha_inicio: date, fecha_fin: date, descripcion: str,
                 tecnicos_asignados: Optional[List[int]] = None,  # IDs de User
                 cuerpos_de_agua_asignados: Optional[List[int]] = None,  # IDs de CuerpoDeAgua
                 id: Optional[int] = None):
        # Validaciones fundamentales
        self._validar_fechas(fecha_inicio, fecha_fin)
        self._validar_descripcion(descripcion)

        # Asignación de valores
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.descripcion = descripcion
        self.tecnicos_asignados = tecnicos_asignados or []
        self.cuerpos_de_agua_asignados = cuerpos_de_agua_asignados or []

        # Validaciones adicionales (IDs válidos)
        self._validar_tecnicos(self.tecnicos_asignados)
        self._validar_cuerpos_de_agua(self.cuerpos_de_agua_asignados)

    @staticmethod
    def _validar_fechas(fecha_inicio: date, fecha_fin: date):
        if fecha_inicio > fecha_fin:
            raise SalidaDeCampoException("La fecha de inicio no puede ser posterior a la fecha de fin.")

    @staticmethod
    def _validar_descripcion(descripcion: str):
        if not descripcion.strip():
            raise SalidaDeCampoException("La descripción no puede estar vacía o ser solo espacios en blanco.")

    @staticmethod
    def _validar_tecnicos(tecnicos_asignados: List[int]):
        if not all(isinstance(tecnico, int) for tecnico in tecnicos_asignados):
            raise SalidaDeCampoException("Todos los técnicos asignados deben ser identificadores válidos (enteros).")

    @staticmethod
    def _validar_cuerpos_de_agua(cuerpos_de_agua_asignados: List[int]):
        if not all(isinstance(cuerpo, int) for cuerpo in cuerpos_de_agua_asignados):
            raise SalidaDeCampoException(
                "Todos los cuerpos de agua asignados deben ser identificadores válidos (enteros)."
            )

    def actualizar(self, fecha_inicio: Optional[date] = None, fecha_fin: Optional[date] = None,
                   descripcion: Optional[str] = None, tecnicos_asignados: Optional[List[int]] = None,
                   cuerpos_de_agua_asignados: Optional[List[int]] = None):
        # Validar y asignar cambios
        if fecha_inicio and fecha_fin:
            self._validar_fechas(fecha_inicio, fecha_fin)
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin

        if descripcion is not None:
            self._validar_descripcion(descripcion)
            self.descripcion = descripcion

        if tecnicos_asignados is not None:
            self._validar_tecnicos(tecnicos_asignados)
            self.tecnicos_asignados = tecnicos_asignados

        if cuerpos_de_agua_asignados is not None:
            self._validar_cuerpos_de_agua(cuerpos_de_agua_asignados)
            self.cuerpos_de_agua_asignados = cuerpos_de_agua_asignados

    def __str__(self):
        return (
            f"SalidaDeCampo(id={self.id}, fecha_inicio={self.fecha_inicio}, "
            f"fecha_fin={self.fecha_fin}, descripcion={self.descripcion})"
        )
