from models.paciente import Paciente

from dataclasses import field
from rest_framework import serializers
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=('usuario','medico')


