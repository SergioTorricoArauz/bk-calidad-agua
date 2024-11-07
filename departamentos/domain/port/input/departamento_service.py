
from abc import ABC, abstractmethod
from typing import List

from departamentos.domain.entities import Departamento


class DepartamentoService(ABC):

    @abstractmethod
    def crear_departamento(self, nombre: str) -> Departamento:
        pass

    @abstractmethod
    def listar_departamentos(self) -> List[Departamento]:
        pass

    @abstractmethod
    def eliminar_departamento(self, nombre: str) -> None:
        pass
