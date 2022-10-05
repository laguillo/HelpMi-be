from rest_framework import serializers
from models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Medico
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Nombre Medico : ': instance.usuario_m.nombre,
            'Apellido Medico : ': instance.usuario_m.apellido,
            'Especialidades : ': instance.id.especialidad,
            'Diagnosticos : ': instance.id.diagnostico,
            
            'Paciente : ':{
            'Nombre Paciente : ': instance.historia.paciente.usuario.nombre,
            'Apellido Paciente : ': instance.historia.paciente.usuario.nombre,
            }
            # 'Historia : ':{
                
            #     'Oximetría : ': instance.historia.familiar.oximetria,
            #     'Frecuencia respiratoria : ': instance.historia.familiar.f_respiratoria,
            #     'Frecuencia cardiaca : ': instance.historia.familiar.f_cardiaca,
            #     'temperatura : ': instance.historia.familiar.temperatura,
            #     'Presion Arterial : ': instance.historia.familiar.p_arterial,
            #     'Glicemias : ': instance.historia.familiar.glicemias

            #  }

        }



