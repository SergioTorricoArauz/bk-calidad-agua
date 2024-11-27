# usuarios/infrastructure/serializers/user_serializer.py

from rest_framework import serializers
from django.contrib.auth.models import User, Group
import re


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']


class UsuarioCrearSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    grupo = serializers.CharField(write_only=True)  # Campo para especificar el grupo

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'grupo']

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo electrónico ya está registrado.")
        return value

    @staticmethod
    def validate_password(value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[A-Za-z]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        return value

    def create(self, validated_data):
        grupo_nombre = validated_data.pop('grupo')  # Extrae el grupo del usuario
        try:
            grupo = Group.objects.get(name=grupo_nombre)
        except Group.DoesNotExist:
            raise serializers.ValidationError(f"El grupo '{grupo_nombre}' no existe.")

        usuario = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        usuario.groups.add(grupo)
        return usuario
