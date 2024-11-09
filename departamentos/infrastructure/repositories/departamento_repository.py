# departamentos/infrastructure/repositories/departamento_repository_impl.py

from typing import List, Optional
from departamentos.domain.entities import Departamento
from departamentos.domain.port.output.departamento_repository import DepartamentoRepository
from departamentos.infrastructure.models import DepartamentoModel
from provincias.domain.entities import Provincia


class DepartamentoRepositoryImpl(DepartamentoRepository):

    def obtener_provincias(self, departamento_id: int) -> List[Provincia]:
        """Obtiene todas las provincias pertenecientes a un departamento específico."""
        try:
            departamento = DepartamentoModel.objects.get(id=departamento_id)
            provincias_model = departamento.provincias.all()  # Usamos el `related_name`
            return [Provincia(nombre=prov.nombre, departamento_id=prov.departamento.id, id=prov.id) for prov in
                    provincias_model]
        except DepartamentoModel.DoesNotExist:
            return []

    def actualizar(self, departamento: Departamento) -> Departamento:
        departamento_model = DepartamentoModel.objects.get(id=departamento.id)
        departamento_model.nombre = departamento.nombre
        departamento_model.save()
        return Departamento(nombre=departamento_model.nombre, id=departamento_model.id)

    def guardar(self, departamento: Departamento) -> Departamento:
        departamento_model = DepartamentoModel.objects.create(nombre=departamento.nombre)
        return Departamento(nombre=departamento_model.nombre, id=departamento_model.id)

    def obtener_por_nombre(self, nombre: str) -> Optional[Departamento]:
        try:
            departamento_model = DepartamentoModel.objects.get(nombre=nombre)
            return Departamento(nombre=departamento_model.nombre, id=departamento_model.id)
        except DepartamentoModel.DoesNotExist:
            return None

    def obtener_por_id(self, id: int) -> Optional[Departamento]:
        try:
            departamento_model = DepartamentoModel.objects.get(id=id)
            return Departamento(nombre=departamento_model.nombre, id=departamento_model.id)
        except DepartamentoModel.DoesNotExist:
            return None

    def eliminar(self, nombre: str) -> None:
        DepartamentoModel.objects.filter(nombre=nombre).delete()

    def eliminar_por_id(self, id: int) -> None:
        DepartamentoModel.objects.filter(id=id).delete()

    def obtener_todos(self) -> List[Departamento]:
        departamentos_model = DepartamentoModel.objects.all()
        return [Departamento(nombre=dep.nombre, id=dep.id) for dep in departamentos_model]
