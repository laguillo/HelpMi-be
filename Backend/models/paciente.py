from django.db import models
from Backend.models.enfermero import Enfermero
from Backend.models.historiaClinica import Historia

from Backend.models.medico import Medico
from .familiar import Familiar
from .user import User
class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario_p=models.ForeignKey(User, on_delete=models.CASCADE)   
    familiar_p=models.ForeignKey(Familiar, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia_p=models.ForeignKey(Historia, on_delete=models.CASCADE)
    enfermero_p=models.ForeignKey(Enfermero, on_delete=models.CASCADE)