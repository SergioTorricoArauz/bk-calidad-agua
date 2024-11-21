# analisis_muestreo/domain/ports/output/analisis_turbidez_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_turbidez import AnalisisTurbidez


class AnalisisTurbidezRepository(ABC):
    @abstractmethod
    def guardar(self, analisis: AnalisisTurbidez) -> AnalisisTurbidez:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[AnalisisTurbidez]:
        pass

    @abstractmethod
    def listar_por_salida(self, salida_id: int) -> List[AnalisisTurbidez]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar(self, analisis: AnalisisTurbidez) -> AnalisisTurbidez:
        pass
