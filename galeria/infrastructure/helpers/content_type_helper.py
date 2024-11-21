# galeria/infrastructure/helpers/content_type_helper.py

from django.contrib.contenttypes.models import ContentType


class ContentTypeHelper:
    """
    Clase para manejar la lógica relacionada con ContentType.
    """

    _MAPPING = {
        'salidadecampo': ('salidas_de_campo', 'salidadecampomodel'),
        'analisiscaudal': ('analisis_muestreo', 'analisicaudalmodel'),
        'analisisturbidez': ('analisis_muestreo', 'analisisturbidezmodel'),
    }

    @staticmethod
    def validate_relacionado_tipo(relacionado_tipo_str: str) -> tuple[str, str]:
        """
        Valida y convierte un tipo relacionado a su app_label y model_name.

        :param relacionado_tipo_str: Tipo relacionado (ej. 'salidadecampo').
        :return: Tuple (app_label, model_name).
        :raises ValueError: Si el tipo relacionado no es válido.
        """
        if relacionado_tipo_str not in ContentTypeHelper._MAPPING:
            raise ValueError(f"Tipo relacionado inválido: {relacionado_tipo_str}.")
        return ContentTypeHelper._MAPPING[relacionado_tipo_str]

    @staticmethod
    def get_content_type(app_label: str, model_name: str) -> ContentType:
        """
        Obtiene el ContentType correspondiente a una app_label y model_name.

        :param app_label: Etiqueta de la aplicación (ej. 'salidas_de_campo').
        :param model_name: Nombre del modelo (ej. 'salidadecampomodel').
        :return: ContentType correspondiente.
        :raises ValueError: Si el ContentType no existe.
        """
        try:
            return ContentType.objects.get(app_label=app_label, model=model_name)
        except ContentType.DoesNotExist:
            raise ValueError(f"ContentType no encontrado para app_label='{app_label}', model_name='{model_name}'.")

    @staticmethod
    def get_related_object(content_type: ContentType, relacionado_id: int):
        """
        Obtiene el objeto relacionado basado en un ContentType y un ID.

        :param content_type: ContentType del objeto relacionado.
        :param relacionado_id: ID del objeto relacionado.
        :return: Instancia del modelo relacionado.
        :raises ValueError: Si el objeto relacionado no existe.
        """
        relacionado_model = content_type.model_class()
        try:
            return relacionado_model.objects.get(id=relacionado_id)
        except relacionado_model.DoesNotExist:
            raise ValueError(f"ID relacionado no encontrado: {relacionado_id} para ContentType '{content_type}'.")

    @staticmethod
    def get_content_type_and_object(relacionado_tipo_str: str, relacionado_id: int):
        """
        Obtiene el ContentType y el objeto relacionado según el tipo y el ID.

        :param relacionado_tipo_str: Tipo relacionado (ej. 'salidadecampo').
        :param relacionado_id: ID del objeto relacionado.
        :return: Tuple[ContentType, object].
        :raises ValueError: Si el tipo relacionado o el ID no son válidos.
        """
        # Validar tipo relacionado
        app_label, model_name = ContentTypeHelper.validate_relacionado_tipo(relacionado_tipo_str)

        # Obtener ContentType
        content_type = ContentTypeHelper.get_content_type(app_label, model_name)

        # Obtener el objeto relacionado
        relacionado_obj = ContentTypeHelper.get_related_object(content_type, relacionado_id)

        return content_type, relacionado_obj

    @classmethod
    def get_mapping(cls, relacionado_tipo_str):
        """
        Obtiene el mapeo de un tipo relacionado.

        :param relacionado_tipo_str: Tipo relacionado (ej. 'salidadecampo').
        :return: Tuple (app_label, model_name).
        """
        return cls._MAPPING[relacionado_tipo_str]
