# provincias/infrastructure/repositories/provincia_repository_impl.py

from typing import List, Optional
from provincias.domain.entities import Provincia
from provincias.domain.ports.output.provincia_repository import ProvinciaRepository
from provincias.infrastructure.models.provincia_model import ProvinciaModel

class ProvinciaRepositoryImpl(ProvinciaRepository):
    def guardar(self, provincia: Provincia) -> Provincia:
        provincia_model = ProvinciaModel.objects.create(
            nombre=provincia.nombre,
            departamento_id=provincia.departamento_id  # Guardar usando departamento_id
        )
        return Provincia(nombre=provincia_model.nombre, departamento_id=provincia_model.departamento.id, id=provincia_model.id)

    def obtener_por_id(self, id: int) -> Optional[Provincia]:
        try:
            provincia_model = ProvinciaModel.objects.get(id=id)
            return Provincia(nombre=provincia_model.nombre, departamento_id=provincia_model.departamento.id, id=provincia_model.id)
        except ProvinciaModel.DoesNotExist:
            return None

    def obtener_por_nombre(self, nombre: str) -> Optional[Provincia]:
        try:
            provincia_model = ProvinciaModel.objects.get(nombre=nombre)
            return Provincia(nombre=provincia_model.nombre, departamento_id=provincia_model.departamento.id, id=provincia_model.id)
        except ProvinciaModel.DoesNotExist:
            return None

    def obtener_por_departamento_id(self, departamento_id: int) -> List[Provincia]:
        provincias_model = ProvinciaModel.objects.filter(departamento_id=departamento_id)
        return [Provincia(nombre=prov.nombre, departamento_id=prov.departamento.id, id=prov.id) for prov in provincias_model]

    def eliminar(self, id: int) -> None:
        ProvinciaModel.objects.filter(id=id).delete()

    def obtener_todas(self) -> List[Provincia]:
        provincias_model = ProvinciaModel.objects.all()
        return [Provincia(nombre=prov.nombre, departamento_id=prov.departamento.id, id=prov.id) for prov in provincias_model]

    def actualizar(self, provincia: Provincia) -> Provincia:
        """Actualiza una provincia existente en la base de datos."""
        provincia_model = ProvinciaModel.objects.get(id=provincia.id)
        provincia_model.nombre = provincia.nombre
        provincia_model.departamento_id = provincia.departamento_id
        provincia_model.save()
        return Provincia(nombre=provincia_model.nombre, departamento_id=provincia_model.departamento.id, id=provincia_model.id)
