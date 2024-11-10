# comunidades/domain/ports/input/comunidad_service.py

from abc import ABC, abstractmethod
from typing import List, Optional
from comunidades.domain.entities.comunidad import Comunidad


class ComunidadService(ABC):
    @abstractmethod
    def crear_comunidad(self, nombre: str, provincia_id: int) -> Comunidad:
        pass

    @abstractmethod
    def listar_comunidades(self) -> List[Comunidad]:
        pass

    @abstractmethod
    def obtener_comunidad_por_id(self, id: int) -> Optional[Comunidad]:
        pass

    @abstractmethod
    def eliminar_comunidad(self, id: int) -> None:
        pass
