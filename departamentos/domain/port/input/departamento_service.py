# departamentos/domain/ports/input/departamento_service.py

from abc import ABC, abstractmethod
from typing import List, Optional

from departamentos.domain.entities import Departamento


class DepartamentoService(ABC):

    @abstractmethod
    def crear_departamento(self, nombre: str) -> Departamento:
        pass

    @abstractmethod
    def listar_departamentos(self) -> List[Departamento]:
        pass

    @abstractmethod
    def obtener_departamento_por_id(self, id: int) -> Optional[Departamento]:
        pass

    @abstractmethod
    def eliminar_departamento(self, nombre: str) -> None:
        pass

    @abstractmethod
    def actualizar_departamento(self, id: int, nombre: str) -> Departamento:
        pass
