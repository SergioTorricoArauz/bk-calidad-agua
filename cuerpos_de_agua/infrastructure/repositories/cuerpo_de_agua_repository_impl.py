# cuerpos_de_agua/infrastructure/repositories/cuerpo_de_agua_repository_impl.py

from typing import List, Optional
from cuerpos_de_agua.domain.entities.cuerpo_de_agua import CuerpoDeAgua
from cuerpos_de_agua.domain.ports.output.cuerpo_de_agua_repository import CuerpoDeAguaRepository
from cuerpos_de_agua.infrastructure.models.cuerpo_de_agua_model import CuerpoDeAguaModel


class CuerpoDeAguaRepositoryImpl(CuerpoDeAguaRepository):

    def guardar(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        cuerpo_de_agua_model = CuerpoDeAguaModel.objects.create(
            nombre=cuerpo_de_agua.nombre,
            tipo=cuerpo_de_agua.tipo,
            latitud=cuerpo_de_agua.latitud,
            longitud=cuerpo_de_agua.longitud,
            comunidad_id=cuerpo_de_agua.comunidad_id
        )
        return CuerpoDeAgua(
            id=cuerpo_de_agua_model.id,
            nombre=cuerpo_de_agua_model.nombre,
            tipo=cuerpo_de_agua_model.tipo,
            latitud=cuerpo_de_agua_model.latitud,
            longitud=cuerpo_de_agua_model.longitud,
            comunidad_id=cuerpo_de_agua_model.comunidad_id
        )

    def obtener_por_id(self, id: int) -> Optional[CuerpoDeAgua]:
        try:
            cuerpo_de_agua_model = CuerpoDeAguaModel.objects.get(id=id)
            return CuerpoDeAgua(
                id=cuerpo_de_agua_model.id,
                nombre=cuerpo_de_agua_model.nombre,
                tipo=cuerpo_de_agua_model.tipo,
                latitud=cuerpo_de_agua_model.latitud,
                longitud=cuerpo_de_agua_model.longitud,
                comunidad_id=cuerpo_de_agua_model.comunidad_id
            )
        except CuerpoDeAguaModel.DoesNotExist:
            return None

    def eliminar(self, id: int) -> None:
        CuerpoDeAguaModel.objects.filter(id=id).delete()

    def actualizar(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        cuerpo_de_agua_model = CuerpoDeAguaModel.objects.get(id=cuerpo_de_agua.id)
        cuerpo_de_agua_model.nombre = cuerpo_de_agua.nombre
        cuerpo_de_agua_model.tipo = cuerpo_de_agua.tipo
        cuerpo_de_agua_model.latitud = cuerpo_de_agua.latitud
        cuerpo_de_agua_model.longitud = cuerpo_de_agua.longitud
        cuerpo_de_agua_model.comunidad_id = cuerpo_de_agua.comunidad_id
        cuerpo_de_agua_model.save()
        return cuerpo_de_agua

    def obtener_todos(self) -> List[CuerpoDeAgua]:
        cuerpos_de_agua_model = CuerpoDeAguaModel.objects.all()
        return [
            CuerpoDeAgua(
                id=cuerpo.id,
                nombre=cuerpo.nombre,
                tipo=cuerpo.tipo,
                latitud=cuerpo.latitud,
                longitud=cuerpo.longitud,
                comunidad_id=cuerpo.comunidad_id
            ) for cuerpo in cuerpos_de_agua_model
        ]
