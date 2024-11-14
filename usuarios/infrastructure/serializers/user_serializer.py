# usuarios/infrastructure/serializers/user_serializer.py

from rest_framework import serializers
from django.contrib.auth.models import User, Group


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

    def create(self, validated_data):
        grupo_nombre = validated_data.pop('grupo')
        usuario = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Asigna el grupo
        grupo = Group.objects.get(name=grupo_nombre)
        usuario.groups.add(grupo)

        return usuario
