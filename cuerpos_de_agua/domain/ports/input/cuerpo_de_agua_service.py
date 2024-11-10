# cuerpos_de_agua/domain/ports/input/cuerpo_de_agua_service.py

from abc import ABC, abstractmethod
from typing import List, Optional
from cuerpos_de_agua.domain.entities.cuerpo_de_agua import CuerpoDeAgua


class CuerpoDeAguaService(ABC):
    @abstractmethod
    def crear_cuerpo_de_agua(self, nombre: str, tipo: str, latitud: Optional[float], longitud: Optional[float],
                             comunidad_id: int) -> CuerpoDeAgua:
        pass

    @abstractmethod
    def listar_cuerpos_de_agua(self) -> List[CuerpoDeAgua]:
        pass

    @abstractmethod
    def obtener_cuerpo_de_agua_por_id(self, id: int) -> Optional[CuerpoDeAgua]:
        pass

    @abstractmethod
    def eliminar_cuerpo_de_agua(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar_cuerpo_de_agua(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        pass
