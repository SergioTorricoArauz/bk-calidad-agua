from datetime import date
from typing import List, Optional

from django.contrib.auth.models import User
from cuerpos_de_agua.infrastructure.models import CuerpoDeAguaModel
from salidas_de_campo.domain.entities.salida_de_campo import SalidaDeCampo
from salidas_de_campo.domain.exceptions import SalidaDeCampoException
from salidas_de_campo.domain.ports.input.salida_de_campo_service import SalidaDeCampoService
from salidas_de_campo.domain.ports.output.salida_de_campo_repository import SalidaDeCampoRepository


class SalidaDeCampoServiceImpl(SalidaDeCampoService):
    def __init__(self, salida_de_campo_repository: SalidaDeCampoRepository):
        self.salida_de_campo_repository = salida_de_campo_repository

    def crear_salida(self, fecha_inicio: date, fecha_fin: date, descripcion: str,
                     tecnicos_asignados: List[int], cuerpos_de_agua_asignados: List[int]) -> SalidaDeCampo:
        # Validar IDs de técnicos
        tecnicos = list(User.objects.filter(id__in=tecnicos_asignados))
        if len(tecnicos) != len(tecnicos_asignados):
            raise SalidaDeCampoException(
                f"Error: Uno o más técnicos asignados no existen. IDs válidos: {[tecnico.id for tecnico in tecnicos]}"
            )

        # Validar IDs de cuerpos de agua
        cuerpos_de_agua_models = list(CuerpoDeAguaModel.objects.filter(id__in=cuerpos_de_agua_asignados))
        if len(cuerpos_de_agua_models) != len(cuerpos_de_agua_asignados):
            raise SalidaDeCampoException(
                f"Error: Uno o más cuerpos de agua asignados no existen. IDs válidos: "
                f"{[cuerpo.id for cuerpo in cuerpos_de_agua_models]}"
            )

        # Crear instancia de la entidad
        salida_de_campo = SalidaDeCampo(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            descripcion=descripcion,
            tecnicos_asignados=[tecnico.id for tecnico in tecnicos],
            cuerpos_de_agua_asignados=[cuerpo.id for cuerpo in cuerpos_de_agua_models]
        )

        return self.salida_de_campo_repository.guardar(salida_de_campo)

    def obtener_salida_por_id(self, id: int) -> Optional[SalidaDeCampo]:
        salida = self.salida_de_campo_repository.obtener_por_id(id)
        if not salida:
            raise SalidaDeCampoException(f"No se encontró una salida de campo con ID {id}.")
        return salida

    def listar_salidas(self, tecnico_id: Optional[int] = None) -> List[SalidaDeCampo]:
        salidas = self.salida_de_campo_repository.obtener_todas(tecnico_id=tecnico_id)
        if tecnico_id and not salidas:
            raise SalidaDeCampoException(f"No se encontraron salidas de campo para el técnico con ID {tecnico_id}.")
        return salidas

    def editar_salida(self, id: int, **datos) -> SalidaDeCampo:
        salida = self.obtener_salida_por_id(id)

        # Actualizar usando el método `actualizar` de la entidad
        salida.actualizar(
            fecha_inicio=datos.get('fecha_inicio'),
            fecha_fin=datos.get('fecha_fin'),
            descripcion=datos.get('descripcion'),
            tecnicos_asignados=datos.get('tecnicos_asignados'),
            cuerpos_de_agua_asignados=datos.get('cuerpos_de_agua_asignados')
        )

        return self.salida_de_campo_repository.actualizar(salida)

    def eliminar_salida(self, id: int) -> None:
        salida = self.obtener_salida_por_id(id)
        if not salida:
            raise SalidaDeCampoException(f"No se encontró la salida de campo con ID {id}.")
        self.salida_de_campo_repository.eliminar(id)

    def filtrar_salidas(self, tecnico_id: Optional[int] = None, fecha_inicio: Optional[date] = None,
                        fecha_fin: Optional[date] = None) -> List[SalidaDeCampo]:
        salidas = self.salida_de_campo_repository.obtener_todas(tecnico_id=tecnico_id)

        if fecha_inicio:
            salidas = [salida for salida in salidas if salida.fecha_inicio >= fecha_inicio]

        if fecha_fin:
            salidas = [salida for salida in salidas if salida.fecha_fin <= fecha_fin]

        if not salidas:
            raise SalidaDeCampoException("No se encontraron salidas de campo con los filtros especificados.")
        return salidas
