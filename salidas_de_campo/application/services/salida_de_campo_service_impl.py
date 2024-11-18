# salidas_de_campo/application/services/salida_de_campo_service_impl.py

from typing import List, Optional
from datetime import date

from cuerpos_de_agua.infrastructure.models import CuerpoDeAguaModel
from salidas_de_campo.domain.entities.salida_de_campo import SalidaDeCampo
from salidas_de_campo.domain.exceptions import SalidaDeCampoException
from salidas_de_campo.domain.ports.input.salida_de_campo_service import SalidaDeCampoService
from salidas_de_campo.domain.ports.output.salida_de_campo_repository import SalidaDeCampoRepository
from django.contrib.auth.models import User


class SalidaDeCampoServiceImpl(SalidaDeCampoService):
    def __init__(self, salida_de_campo_repository: SalidaDeCampoRepository):
        self.salida_de_campo_repository = salida_de_campo_repository

    def crear_salida(self, fecha_inicio: date, fecha_fin: date, descripcion: str,
                     tecnicos_asignados: List[int], cuerpos_de_agua_asignados: List[int]) -> SalidaDeCampo:
        # Obtiene objetos User y CuerpoDeAguaModel a partir de los IDs
        tecnicos = list(User.objects.filter(id__in=tecnicos_asignados))
        if len(tecnicos) != len(tecnicos_asignados):
            raise SalidaDeCampoException("Uno o más IDs de técnicos no existen.")

        cuerpos_de_agua_models = list(CuerpoDeAguaModel.objects.filter(id__in=cuerpos_de_agua_asignados))
        if len(cuerpos_de_agua_models) != len(cuerpos_de_agua_asignados):
            raise SalidaDeCampoException("Uno o más IDs de cuerpos de agua no existen.")

        # Almacena solo los IDs en lugar de los objetos completos
        salida_de_campo = SalidaDeCampo(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            descripcion=descripcion,
            tecnicos_asignados=[tecnico.id for tecnico in tecnicos],  # Lista de IDs de técnicos
            cuerpos_de_agua_asignados=[cuerpo.id for cuerpo in cuerpos_de_agua_models]
            # Lista de IDs de cuerpos de agua
        )

        return self.salida_de_campo_repository.guardar(salida_de_campo)

    def obtener_salida_por_id(self, id: int) -> Optional[SalidaDeCampo]:
        return self.salida_de_campo_repository.obtener_por_id(id)

    def listar_salidas(self) -> List[SalidaDeCampo]:
        return self.salida_de_campo_repository.obtener_todas()

    def editar_salida(self, id: int, **datos) -> SalidaDeCampo:
        salida = self.obtener_salida_por_id(id)
        if not salida:
            raise SalidaDeCampoException(f"Salida de campo con id {id} no encontrada.")

        # Actualización de datos
        salida.fecha_inicio = datos.get('fecha_inicio', salida.fecha_inicio)
        salida.fecha_fin = datos.get('fecha_fin', salida.fecha_fin)
        salida.descripcion = datos.get('descripcion', salida.descripcion)

        # Actualización de técnicos asignados
        tecnicos_asignados = datos.get('tecnicos_asignados')
        if tecnicos_asignados:
            # Obtiene solo los IDs de User
            salida.tecnicos_asignados = [tecnico.id for tecnico in User.objects.filter(id__in=tecnicos_asignados)]

        # Actualización de cuerpos de agua asignados
        cuerpos_de_agua_asignados = datos.get('cuerpos_de_agua_asignados')
        if cuerpos_de_agua_asignados:
            # Obtiene solo los IDs de CuerpoDeAguaModel
            cuerpos_de_agua_models = list(CuerpoDeAguaModel.objects.filter(id__in=cuerpos_de_agua_asignados))
            salida.cuerpos_de_agua_asignados = [cuerpo.id for cuerpo in cuerpos_de_agua_models]

        # Guardar los cambios
        return self.salida_de_campo_repository.actualizar(salida)

    def eliminar_salida(self, id: int) -> None:
        salida = self.obtener_salida_por_id(id)
        if not salida:
            raise SalidaDeCampoException(f"Salida de campo con id {id} no encontrada.")

        self.salida_de_campo_repository.eliminar(id)
