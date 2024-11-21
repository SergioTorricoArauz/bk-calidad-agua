# analisis_muestreo/application/service/analisis_caudal_service_impl.py

from typing import List, Optional
from datetime import datetime
from analisis_muestreo.domain.entities.analisis_caudal import AnalisisCaudal
from analisis_muestreo.domain.ports.input.analisis_caudal_service import AnalisisCaudalService
from analisis_muestreo.domain.ports.output.analisis_caudal_repository import AnalisisCaudalRepository
from analisis_muestreo.domain.exception import AnalisisMuestreoException


class AnalisisCaudalServiceImpl(AnalisisCaudalService):
    def __init__(self, repository: AnalisisCaudalRepository):
        self.repository = repository

    def crear_analisis(self, velocidad: float, ancho: float, profundidad_media: float, fecha: datetime,
                       tecnico_id: int, salida_id: int) -> AnalisisCaudal:
        if velocidad <= 0 or ancho <= 0 or profundidad_media <= 0:
            raise AnalisisMuestreoException("Los valores de velocidad, ancho y profundidad deben ser positivos.")
        analisis = AnalisisCaudal(
            velocidad=velocidad,
            ancho=ancho,
            profundidad_media=profundidad_media,
            fecha=fecha,
            tecnico_id=tecnico_id,
            salida_id=salida_id
        )
        return self.repository.guardar(analisis)

    def obtener_analisis_por_id(self, id: int) -> Optional[AnalisisCaudal]:
        return self.repository.obtener_por_id(id)

    def listar_analisis_por_salida(self, salida_id: int) -> List[AnalisisCaudal]:
        return self.repository.listar_por_salida(salida_id)

    def eliminar_analisis(self, id: int) -> None:
        self.repository.eliminar(id)

    def actualizar_analisis(self, id: int, velocidad: float, ancho: float,
                            profundidad_media: float, fecha: datetime, tecnico_id: int,
                            salida_id: int) -> AnalisisCaudal:
        analisis = self.obtener_analisis_por_id(id)
        if not analisis:
            raise AnalisisMuestreoException(f"No se encontró el análisis de caudal con ID {id}.")

        analisis.velocidad = velocidad
        analisis.ancho = ancho
        analisis.profundidad_media = profundidad_media
        analisis.fecha = fecha
        analisis.tecnico_id = tecnico_id
        analisis.salida_id = salida_id
        return self.repository.actualizar(analisis)
