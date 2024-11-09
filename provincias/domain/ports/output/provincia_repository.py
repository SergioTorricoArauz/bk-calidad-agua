# provincias/domain/ports/output/provincia_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from provincias.domain.entities import Provincia


class ProvinciaRepository(ABC):
    @abstractmethod
    def guardar(self, provincia: Provincia) -> Provincia:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Provincia]:
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Provincia]:
        pass

    @abstractmethod
    def obtener_por_departamento_id(self, departamento_id: int) -> List[Provincia]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def obtener_todas(self) -> List[Provincia]:
        pass

    @abstractmethod
    def actualizar(self, provincia):
        pass

# @abstractmethod
# def obtener_provincias_por_departamento(self, departamento_id):
#   pass
