from rest_framework import serializers

from models.paciente import Paciente

from dataclasses import field


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['usuario', 'medico']
