from django.db import models

from .user import User
from .paciente import Paciente
from .familiar import Familiar
from .medico import Medico


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)
    familiar=models.ForeignKey(Familiar, related_name='paciente', on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE)



