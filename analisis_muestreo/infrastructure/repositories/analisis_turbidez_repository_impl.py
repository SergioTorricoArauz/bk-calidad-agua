# analisis_muestreo/infrastructure/repositories/analisis_turbidez_repository_impl.py
from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_turbidez import AnalisisTurbidez
from analisis_muestreo.domain.ports.output.analisis_turbidez_repository import AnalisisTurbidezRepository
from analisis_muestreo.infrastructure.models.analisis_turbidez_model import AnalisisTurbidezModel


class AnalisisTurbidezRepositoryImpl(AnalisisTurbidezRepository):
    def actualizar(self, analisis: AnalisisTurbidez) -> AnalisisTurbidez:
        model = AnalisisTurbidezModel.objects.get(id=analisis.id)
        model.ntu = analisis.ntu
        model.fecha = analisis.fecha
        model.tecnico_id = analisis.tecnico_id
        model.salida_id = analisis.salida_id
        model.save()
        return AnalisisTurbidez(
            id=model.id,
            ntu=model.ntu,
            fecha=model.fecha,
            tecnico_id=model.tecnico_id,
            salida_id=model.salida_id
        )

    def guardar(self, analisis: AnalisisTurbidez) -> AnalisisTurbidez:
        model = AnalisisTurbidezModel.objects.create(
            ntu=analisis.ntu,
            fecha=analisis.fecha,
            tecnico_id=analisis.tecnico_id,
            salida_id=analisis.salida_id
        )
        return AnalisisTurbidez(
            id=model.id,
            ntu=model.ntu,
            fecha=model.fecha,
            tecnico_id=model.tecnico_id,
            salida_id=model.salida_id
        )

    def obtener_por_id(self, id: int) -> Optional[AnalisisTurbidez]:
        try:
            model = AnalisisTurbidezModel.objects.get(id=id)
            return AnalisisTurbidez(
                id=model.id,
                ntu=model.ntu,
                fecha=model.fecha,
                tecnico_id=model.tecnico_id,
                salida_id=model.salida_id
            )
        except AnalisisTurbidezModel.DoesNotExist:
            return None

    def listar_por_salida(self, salida_id: int) -> List[AnalisisTurbidez]:
        models = AnalisisTurbidezModel.objects.filter(salida_id=salida_id)
        return [
            AnalisisTurbidez(
                id=model.id,
                ntu=model.ntu,
                fecha=model.fecha,
                tecnico_id=model.tecnico_id,
                salida_id=model.salida_id
            ) for model in models
        ]

    def eliminar(self, id: int) -> None:
        AnalisisTurbidezModel.objects.filter(id=id).delete()
