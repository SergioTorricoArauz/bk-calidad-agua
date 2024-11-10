# cuerpos_de_agua/domain/ports/output/cuerpo_de_agua_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from cuerpos_de_agua.domain.entities.cuerpo_de_agua import CuerpoDeAgua


class CuerpoDeAguaRepository(ABC):
    @abstractmethod
    def guardar(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[CuerpoDeAgua]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[CuerpoDeAgua]:
        pass
