from django.db import models

from Backend.models.historiaClinica import Historia
from .user import User, models

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        User, related_name='medico', on_delete=models.CASCADE)
    especialidad = models.CharField('Especialidad', max_length=45)
    diagnostico = models.CharField('Diagnostico', max_length=400)
    historia = models.ForeignKey(Historia, related_name='paciente', on_delete=models.CASCADE)