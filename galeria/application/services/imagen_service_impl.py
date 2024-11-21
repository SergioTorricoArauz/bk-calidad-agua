# galeria/application/services/imagen_service_impl.py

from typing import List, Optional
from galeria.domain.entities.imagen import Imagen
from galeria.domain.ports.input.imagen_service import ImagenService
from galeria.domain.ports.output.imagen_repository import ImagenRepository


class ImagenServiceImpl(ImagenService):
    def __init__(self, repository: ImagenRepository):
        self.repository = repository

    def crear_imagen(self, url: str, relacionado_tipo: str, relacionado_id: int) -> Imagen:
        imagen = Imagen(url=url, relacionado_tipo=relacionado_tipo, relacionado_id=relacionado_id)
        return self.repository.guardar(imagen)

    def obtener_imagen_por_id(self, id: int) -> Optional[Imagen]:
        return self.repository.obtener_por_id(id)

    def listar_imagenes_por_relacion(self, relacionado_tipo: str, relacionado_id: int) -> List[Imagen]:
        return self.repository.listar_por_relacion(relacionado_tipo, relacionado_id)

    def eliminar_imagen(self, id: int) -> None:
        self.repository.eliminar(id)
