# comunidades/infrastructure/repositories/comunidad_repository_impl.py

from typing import List, Optional
from comunidades.domain.entities.comunidad import Comunidad
from comunidades.domain.ports.output.comunidad_repository import ComunidadRepository
from comunidades.infrastructure.models.comunidad_model import ComunidadModel


class ComunidadRepositoryImpl(ComunidadRepository):
    def actualizar(self, comunidad):
        comunidad_model = ComunidadModel.objects.get(id=comunidad.id)
        comunidad_model.nombre = comunidad.nombre
        comunidad_model.provincia_id = comunidad.provincia_id
        comunidad_model.save()
        return Comunidad(id=comunidad_model.id, nombre=comunidad_model.nombre,
                         provincia_id=comunidad_model.provincia.id)

    def guardar(self, comunidad: Comunidad) -> Comunidad:
        comunidad_model = ComunidadModel.objects.create(
            nombre=comunidad.nombre,
            provincia_id=comunidad.provincia_id
        )
        return Comunidad(id=comunidad_model.id, nombre=comunidad_model.nombre,
                         provincia_id=comunidad_model.provincia_id)

    def obtener_por_id(self, id: int) -> Optional[Comunidad]:
        try:
            comunidad_model = ComunidadModel.objects.get(id=id)
            return Comunidad(id=comunidad_model.id, nombre=comunidad_model.nombre,
                             provincia_id=comunidad_model.provincia.id)
        except ComunidadModel.DoesNotExist:
            return None

    def obtener_todas(self) -> List[Comunidad]:
        comunidades_model = ComunidadModel.objects.all()
        return [Comunidad(id=cm.id, nombre=cm.nombre, provincia_id=cm.provincia.id) for cm in comunidades_model]

    def eliminar(self, id: int) -> None:
        ComunidadModel.objects.filter(id=id).delete()
