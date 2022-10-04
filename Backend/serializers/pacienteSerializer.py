from rest_framework import serializers
from models.paciente import Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Nombre Paciente :': instance.usuario.nombre,
            'Apellido Paciente :': instance.usuario.apellido,
            'Medico :': instance.medico,






        }


