# usuarios/signals.py

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)


@receiver(post_migrate)
def crear_grupos_por_defecto(sender, **kwargs):
    if sender.name == 'usuarios':
        grupos = ['Administrador', 'Técnico']
        for nombre_grupo in grupos:
            grupo, creado = Group.objects.get_or_create(name=nombre_grupo)
            if creado:
                logger.info(f"Grupo '{nombre_grupo}' creado exitosamente.")
            else:
                logger.info(f"Grupo '{nombre_grupo}' ya existe.")
