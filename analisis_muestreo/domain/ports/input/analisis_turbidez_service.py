from abc import ABC, abstractmethod
from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_turbidez import AnalisisTurbidez


class AnalisisTurbidezService(ABC):
    @abstractmethod
    def crear_analisis(self, ntu: float, fecha, tecnico_id: int, salida_id: int) -> AnalisisTurbidez:
        pass

    @abstractmethod
    def obtener_analisis_por_id(self, id: int) -> Optional[AnalisisTurbidez]:
        pass

    @abstractmethod
    def listar_analisis_por_salida(self, salida_id: int) -> List[AnalisisTurbidez]:
        pass

    @abstractmethod
    def eliminar_analisis(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar_analisis(self, id: int, ntu: float, fecha, tecnico_id: int, salida_id: int) -> AnalisisTurbidez:
        pass
