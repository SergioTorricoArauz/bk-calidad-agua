# galeria/infrastructure/repositories/imagen_repository_impl.py

from typing import List, Optional
from galeria.domain.entities.imagen import Imagen
from galeria.domain.ports.output.imagen_repository import ImagenRepository
from galeria.infrastructure.models.imagen_model import ImagenModel
from django.contrib.contenttypes.models import ContentType


class ImagenRepositoryImpl(ImagenRepository):
    def guardar(self, imagen: Imagen) -> Imagen:
        content_type = ContentType.objects.get(model=imagen.relacionado_tipo.lower())
        model = ImagenModel.objects.create(
            url=imagen.url,
            relacionado_tipo=content_type,
            relacionado_id=imagen.relacionado_id
        )
        return Imagen(
            id=model.id,
            url=model.url,
            relacionado_tipo=model.relacionado_tipo.model,
            relacionado_id=model.relacionado_id
        )

    def obtener_por_id(self, id: int) -> Optional[Imagen]:
        try:
            model = ImagenModel.objects.get(id=id)
            return Imagen(
                id=model.id,
                url=model.url,
                relacionado_tipo=model.relacionado_tipo.model,
                relacionado_id=model.relacionado_id
            )
        except ImagenModel.DoesNotExist:
            return None

    def listar_por_relacion(self, relacionado_tipo: str, relacionado_id: int) -> List[Imagen]:
        content_type = ContentType.objects.get(model=relacionado_tipo.lower())
        models = ImagenModel.objects.filter(relacionado_tipo=content_type, relacionado_id=relacionado_id)
        return [
            Imagen(
                id=model.id,
                url=model.url,
                relacionado_tipo=model.relacionado_tipo.model,
                relacionado_id=model.relacionado_id
            )
            for model in models
        ]

    def eliminar(self, id: int) -> None:
        ImagenModel.objects.filter(id=id).delete()
