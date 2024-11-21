# galeria/domain/ports/input/imagen_service.py

from abc import ABC, abstractmethod
from typing import List, Optional
from galeria.domain.entities.imagen import Imagen


class ImagenService(ABC):
    @abstractmethod
    def crear_imagen(self, url: str, relacionado_tipo: str, relacionado_id: int) -> Imagen:
        pass

    @abstractmethod
    def obtener_imagen_por_id(self, id: int) -> Optional[Imagen]:
        pass

    @abstractmethod
    def listar_imagenes_por_relacion(self, relacionado_tipo: str, relacionado_id: int) -> List[Imagen]:
        pass

    @abstractmethod
    def eliminar_imagen(self, id: int) -> None:
        pass
