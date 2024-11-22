# galeria/infrastructure/models/imagen_model.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ImagenModel(models.Model):
    url = models.ImageField(upload_to='galeria/')  # URL de la imagen
    relacionado_tipo = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Modelo relacionado
    relacionado_id = models.PositiveIntegerField()  # ID del objeto relacionado
    relacionado_objeto = GenericForeignKey('relacionado_tipo', 'relacionado_id')  # Referencia genérica

    def __str__(self):
        return f"Imagen(URL: {self.url}, Relacionado: {self.relacionado_tipo} - ID {self.relacionado_id})"
