from rest_framework import serializers
from Backend.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Medico
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Nombre Medico : ': instance.usuario.nombre,
            'Apellido Medico : ': instance.usuario.apellido,
            'Especialidades : ': instance.id.especialidad,
            'Diagnosticos : ': instance.id.diagnostico,
            'Nombre Paciente : ': instance.historia.paciente.usuario.nombre,
            'Apellido Paciente : ': instance.historia.paciente.usuario.nombre,

            'Historia : ':{
                
                'Oximetría : ': instance.historia.familiar.oximetria,
                'Frecuencia respiratoria : ': instance.historia.familiar.f_respiratoria,
                'Frecuencia cardiaca : ': instance.historia.familiar.f_cardiaca,
                'temperatura : ': instance.historia.familiar.temperatura,
                'Presion Arterial : ': instance.historia.familiar.p_arterial,
                'Glicemias : ': instance.historia.familiar.glicemias,

             }

        }



