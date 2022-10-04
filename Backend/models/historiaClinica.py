from django.db import models
from Backend.models.familiar import Familiar
from Backend.models.medico import Medico

from Backend.models.paciente import Paciente
from Backend.models.user import User


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)
    familiar=models.ForeignKey(Familiar, related_name='paciente', on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE)



