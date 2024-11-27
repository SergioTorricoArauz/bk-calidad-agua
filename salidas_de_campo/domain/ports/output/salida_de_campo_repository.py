# salidas_de_campo/domain/ports/output/salida_de_campo_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from salidas_de_campo.domain.entities.salida_de_campo import SalidaDeCampo


class SalidaDeCampoRepository(ABC):
    @abstractmethod
    def guardar(self, salida: SalidaDeCampo) -> SalidaDeCampo:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[SalidaDeCampo]:
        pass

    @abstractmethod
    def obtener_todas(self, tecnico_id: Optional[int] = None) -> List[SalidaDeCampo]:
        pass

    @abstractmethod
    def actualizar(self, salida: SalidaDeCampo) -> SalidaDeCampo:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass
