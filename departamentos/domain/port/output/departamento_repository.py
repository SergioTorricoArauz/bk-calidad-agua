# mi_app/domain/ports/output/departamento_repository.py

from abc import ABC, abstractmethod
from typing import Optional

from departamentos.domain.entities import Departamento


class DepartamentoRepository(ABC):

    @abstractmethod
    def guardar(self, departamento: Departamento) -> None:
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Departamento]:
        pass

    @abstractmethod
    def eliminar(self, nombre: str) -> None:
        pass
