# galeria/domain/ports/output/imagen_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from galeria.domain.entities.imagen import Imagen


class ImagenRepository(ABC):
    @abstractmethod
    def guardar(self, imagen: Imagen) -> Imagen:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Imagen]:
        pass

    @abstractmethod
    def listar_por_relacion(self, relacionado_tipo: str, relacionado_id: int) -> List[Imagen]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass
