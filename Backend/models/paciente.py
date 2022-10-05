from django.db import models

from .enfermero import Enfermero
from .historiaClinica import Historia
from .medico import Medico
from .familiar import Familiar
from .user import User


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia_p = models.ForeignKey(Historia, on_delete=models.CASCADE)
    enfermero_p = models.ForeignKey(Enfermero, on_delete=models.CASCADE)
