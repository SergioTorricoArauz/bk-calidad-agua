# provincias/domain/ports/input/provincia_service.py

from abc import ABC, abstractmethod
from typing import List, Optional
from provincias.domain.entities import Provincia


class ProvinciaService(ABC):
    @abstractmethod
    def crear_provincia(self, nombre: str, departamento_id: int) -> Provincia:
        pass

    @abstractmethod
    def listar_provincias(self) -> List[Provincia]:
        pass

    @abstractmethod
    def obtener_provincia_por_id(self, id: int) -> Optional[Provincia]:
        pass

    @abstractmethod
    def eliminar_provincia(self, id: int) -> None:
        pass
