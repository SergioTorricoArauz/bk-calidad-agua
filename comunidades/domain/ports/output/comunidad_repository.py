# comunidades/domain/ports/output/comunidad_repository_impl.py

from abc import ABC, abstractmethod

from typing import List, Optional
from comunidades.domain.entities.comunidad import Comunidad


class ComunidadRepository(ABC):
    @abstractmethod
    def guardar(self, comunidad: Comunidad) -> Comunidad:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Comunidad]:
        pass

    @abstractmethod
    def obtener_todas(self) -> List[Comunidad]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar(self, comunidad):
        pass
