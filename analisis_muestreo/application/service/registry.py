# analisis/application/registry.py

from typing import Type, Dict

from analisis_muestreo.domain.entities import Analisis, AnalisisTurbidez, AnalisisCaudal, AnalisisPH


class AnalisisRegistry:
    _registry: Dict[str, Type[Analisis]] = {}

    @classmethod
    def registrar(cls, tipo: str, analisis_class: Type[Analisis]):
        """Registra un nuevo tipo de análisis."""
        cls._registry[tipo] = analisis_class

    @classmethod
    def obtener(cls, tipo: str) -> Type[Analisis]:
        """Obtiene la clase asociada a un tipo de análisis."""
        if tipo not in cls._registry:
            raise ValueError(f"Tipo de análisis no soportado: {tipo}")
        return cls._registry[tipo]


# Registrar los tipos disponibles
AnalisisRegistry.registrar("turbidez", AnalisisTurbidez)
AnalisisRegistry.registrar("caudal", AnalisisCaudal)
AnalisisRegistry.registrar("ph", AnalisisPH)
