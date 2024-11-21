# analisis_muestreo/application/services/analisis_turbidez_service_impl.py

from typing import List, Optional
from datetime import datetime
from analisis_muestreo.domain.entities.analisis_turbidez import AnalisisTurbidez
from analisis_muestreo.domain.ports.input.analisis_turbidez_service import AnalisisTurbidezService
from analisis_muestreo.domain.ports.output.analisis_turbidez_repository import AnalisisTurbidezRepository
from analisis_muestreo.domain.exception import AnalisisMuestreoException


class AnalisisTurbidezServiceImpl(AnalisisTurbidezService):
    def __init__(self, repository: AnalisisTurbidezRepository):
        self.repository = repository

    def crear_analisis(self, ntu: float, fecha: datetime, tecnico_id: int, salida_id: int) -> AnalisisTurbidez:
        if ntu < 0:
            raise AnalisisMuestreoException("El valor de NTU no puede ser negativo.")
        analisis = AnalisisTurbidez(ntu=ntu, fecha=fecha, tecnico_id=tecnico_id, salida_id=salida_id)
        return self.repository.guardar(analisis)

    def obtener_analisis_por_id(self, id: int) -> Optional[AnalisisTurbidez]:
        return self.repository.obtener_por_id(id)

    def listar_analisis_por_salida(self, salida_id: int) -> List[AnalisisTurbidez]:
        return self.repository.listar_por_salida(salida_id)

    def eliminar_analisis(self, id: int) -> None:
        self.repository.eliminar(id)

    def actualizar_analisis(self, id: int, ntu: float, fecha: datetime, tecnico_id: int,
                            salida_id: int) -> AnalisisTurbidez:
        analisis = self.obtener_analisis_por_id(id)
        if not analisis:
            raise AnalisisMuestreoException(f"No se encontró el análisis de turbidez con ID {id}.")

        analisis.ntu = ntu
        analisis.fecha = fecha
        analisis.tecnico_id = tecnico_id
        analisis.salida_id = salida_id
        return self.repository.actualizar(analisis)
