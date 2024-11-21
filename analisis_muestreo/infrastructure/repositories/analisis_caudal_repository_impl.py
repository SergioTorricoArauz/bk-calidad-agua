from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_caudal import AnalisisCaudal
from analisis_muestreo.domain.ports.output.analisis_caudal_repository import AnalisisCaudalRepository
from analisis_muestreo.infrastructure.models.analisis_caudal_model import AnalisisCaudalModel


class AnalisisCaudalRepositoryImpl(AnalisisCaudalRepository):
    def actualizar(self, analisis: AnalisisCaudal) -> AnalisisCaudal:
        model = AnalisisCaudalModel.objects.get(id=analisis.id)
        model.velocidad = analisis.velocidad
        model.ancho = analisis.ancho
        model.profundidad_media = analisis.profundidad_media
        model.fecha = analisis.fecha
        model.tecnico_id = analisis.tecnico_id
        model.salida_id = analisis.salida_id
        model.save()
        return AnalisisCaudal(
            id=model.id,
            velocidad=model.velocidad,
            ancho=model.ancho,
            profundidad_media=model.profundidad_media,
            fecha=model.fecha,
            tecnico_id=model.tecnico_id,
            salida_id=model.salida_id
        )

    def guardar(self, analisis: AnalisisCaudal) -> AnalisisCaudal:
        model = AnalisisCaudalModel.objects.create(
            velocidad=analisis.velocidad,
            ancho=analisis.ancho,
            profundidad_media=analisis.profundidad_media,
            fecha=analisis.fecha,
            tecnico_id=analisis.tecnico_id,
            salida_id=analisis.salida_id
        )
        return AnalisisCaudal(
            id=model.id,
            velocidad=model.velocidad,
            ancho=model.ancho,
            profundidad_media=model.profundidad_media,
            fecha=model.fecha,
            tecnico_id=model.tecnico_id,
            salida_id=model.salida_id
        )

    def obtener_por_id(self, id: int) -> Optional[AnalisisCaudal]:
        try:
            model = AnalisisCaudalModel.objects.get(id=id)
            return AnalisisCaudal(
                id=model.id,
                velocidad=model.velocidad,
                ancho=model.ancho,
                profundidad_media=model.profundidad_media,
                fecha=model.fecha,
                tecnico_id=model.tecnico_id,
                salida_id=model.salida_id
            )
        except AnalisisCaudalModel.DoesNotExist:
            return None

    def listar_por_salida(self, salida_id: int) -> List[AnalisisCaudal]:
        models = AnalisisCaudalModel.objects.filter(salida_id=salida_id)
        return [
            AnalisisCaudal(
                id=model.id,
                velocidad=model.velocidad,
                ancho=model.ancho,
                profundidad_media=model.profundidad_media,
                fecha=model.fecha,
                tecnico_id=model.tecnico_id,
                salida_id=model.salida_id
            ) for model in models
        ]

    def eliminar(self, id: int) -> None:
        AnalisisCaudalModel.objects.filter(id=id).delete()
