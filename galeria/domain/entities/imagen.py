# galeria/domain/entities/imagen.py

class Imagen:
    def __init__(self, url: str, relacionado_tipo: str, relacionado_id: int, id: int = None):
        if not url:
            raise ValueError("La URL de la imagen es obligatoria.")
        if relacionado_tipo is None or relacionado_id is None:
            raise ValueError("Debe especificar un tipo y un ID relacionados.")

        self.id = id
        self.url = url
        self.relacionado_tipo = relacionado_tipo  # Nombre del modelo relacionado
        self.relacionado_id = relacionado_id  # ID del objeto relacionado

    def __str__(self):
        return f"Imagen(URL: {self.url}, Relacionado: {self.relacionado_tipo} - ID {self.relacionado_id})"
