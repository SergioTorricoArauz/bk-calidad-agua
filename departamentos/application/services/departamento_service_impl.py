# mi_app/application/services/departamento_service_impl.py

from typing import List, Optional

from departamentos.domain.entities import Departamento
from departamentos.domain.exception import DepartamentoError
from departamentos.domain.port.input import DepartamentoService
from departamentos.domain.port.output.departamento_repository import DepartamentoRepository


class DepartamentoServiceImpl(DepartamentoService):
    """Implementación de los casos de uso relacionados con Departamento."""

    def __init__(self, departamento_repository: DepartamentoRepository):
        self.departamento_repository = departamento_repository

    def crear_departamento(self, nombre: str) -> Departamento:
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacío.")
        departamento = Departamento(nombre=nombre)
        return self.departamento_repository.guardar(departamento)

    def listar_departamentos(self) -> List[Departamento]:
        return self.departamento_repository.obtener_todos()

    def obtener_departamento_por_id(self, id: int) -> Optional[Departamento]:
        departamento = self.departamento_repository.obtener_por_id(id)
        if departamento is None:
            raise DepartamentoError(f"Departamento con id {id} no encontrado.")
        return departamento

    def eliminar_departamento(self, nombre: str) -> None:
        """Elimina un departamento por su nombre"""
        departamento = self.departamento_repository.obtener_por_nombre(nombre)
        if departamento is None:
            raise DepartamentoError(f"Departamento con nombre '{nombre}' no encontrado.")
        self.departamento_repository.eliminar(nombre)
