# salidas_de_campo/infrastructure/repositories/salida_de_campo_repository_impl.py

from typing import List, Optional
from salidas_de_campo.domain.entities.salida_de_campo import SalidaDeCampo
from salidas_de_campo.domain.ports.output.salida_de_campo_repository import SalidaDeCampoRepository
from salidas_de_campo.infrastructure.models.salida_de_campo_model import SalidaDeCampoModel


class SalidaDeCampoRepositoryImpl(SalidaDeCampoRepository):
    def guardar(self, salida: SalidaDeCampo) -> SalidaDeCampo:
        salida_model = SalidaDeCampoModel.objects.create(
            fecha_inicio=salida.fecha_inicio,
            fecha_fin=salida.fecha_fin,
            descripcion=salida.descripcion
        )

        salida_model.tecnicos_asignados.set(salida.tecnicos_asignados)
        salida_model.cuerpos_de_agua_asignados.set(salida.cuerpos_de_agua_asignados)

        salida_model.save()
        salida.id = salida_model.id
        return salida

    def obtener_por_id(self, id: int) -> Optional[SalidaDeCampo]:
        try:
            salida_model = SalidaDeCampoModel.objects.get(id=id)
            return self._convertir_a_entidad(salida_model)
        except SalidaDeCampoModel.DoesNotExist:
            return None

    def obtener_todas(self, tecnico_id: Optional[int] = None) -> List[SalidaDeCampo]:
        if tecnico_id:
            salida_models = SalidaDeCampoModel.objects.filter(tecnicos_asignados__id=tecnico_id)
        else:
            salida_models = SalidaDeCampoModel.objects.all()

        return [self._convertir_a_entidad(salida) for salida in salida_models]

    def actualizar(self, salida: SalidaDeCampo) -> SalidaDeCampo:
        salida_model = SalidaDeCampoModel.objects.get(id=salida.id)
        salida_model.fecha_inicio = salida.fecha_inicio
        salida_model.fecha_fin = salida.fecha_fin
        salida_model.descripcion = salida.descripcion

        salida_model.tecnicos_asignados.set(salida.tecnicos_asignados)
        salida_model.cuerpos_de_agua_asignados.set(salida.cuerpos_de_agua_asignados)

        salida_model.save()
        return salida

    def eliminar(self, id: int) -> None:
        SalidaDeCampoModel.objects.filter(id=id).delete()

    @staticmethod
    def _convertir_a_entidad(salida_model: SalidaDeCampoModel) -> SalidaDeCampo:
        return SalidaDeCampo(
            id=salida_model.id,
            fecha_inicio=salida_model.fecha_inicio,
            fecha_fin=salida_model.fecha_fin,
            descripcion=salida_model.descripcion,
            tecnicos_asignados=[tecnico.id for tecnico in salida_model.tecnicos_asignados.all()],
            cuerpos_de_agua_asignados=[cuerpo.id for cuerpo in salida_model.cuerpos_de_agua_asignados.all()]
        )
