# departamentos/application/services/departamento_service_impl.py

from typing import List, Optional
from departamentos.domain.entities import Departamento
from departamentos.domain.exception import DepartamentoError
from departamentos.domain.port.input import DepartamentoService
from departamentos.domain.port.output.departamento_repository import DepartamentoRepository


class DepartamentoServiceImpl(DepartamentoService):

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

    def actualizar_departamento(self, id: int, nombre: str) -> Departamento:
        departamento = self.obtener_departamento_por_id(id)
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacío.")
        departamento.nombre = nombre
        return self.departamento_repository.actualizar(departamento)

    def eliminar_departamento(self, nombre: str) -> None:
        departamento = self.departamento_repository.obtener_por_nombre(nombre)
        if departamento is None:
            raise DepartamentoError(f"Departamento con nombre '{nombre}' no encontrado.")
        self.departamento_repository.eliminar(nombre)

    def eliminar_departamento_por_id(self, id: int) -> None:
        departamento = self.obtener_departamento_por_id(id)
        if departamento is None:
            raise DepartamentoError(f"Departamento con id '{id}' no encontrado.")
        self.departamento_repository.eliminar_por_id(id)
