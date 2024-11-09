# departamentos/domain/ports/output/departamento_repository.py

from abc import ABC, abstractmethod
from typing import Optional, List
from departamentos.domain.entities import Departamento
from provincias.domain.entities import Provincia


class DepartamentoRepository(ABC):

    @abstractmethod
    def guardar(self, departamento: Departamento) -> Departamento:
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Departamento]:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Departamento]:
        pass

    @abstractmethod
    def eliminar(self, nombre: str) -> None:
        pass

    @abstractmethod
    def eliminar_por_id(self, id: int) -> None:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Departamento]:
        pass

    @abstractmethod
    def actualizar(self, departamento: Departamento) -> Departamento:
        pass

    @abstractmethod
    def obtener_provincias(self, departamento_id: int) -> List[Provincia]:
        pass
