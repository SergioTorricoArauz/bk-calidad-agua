class DepartamentoDTO:
    def __init__(self, nombre: str, id: int = None):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"DepartamentoDTO(id={self.id}, nombre={self.nombre})"
