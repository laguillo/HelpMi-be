from django.db import models

from .historiaClinica import Historia
from .user import User

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_m = models.ForeignKey(
        User, on_delete=models.CASCADE)
    especialidad = models.CharField('Especialidad', max_length=45)
    diagnostico = models.CharField('Diagnostico', max_length=400)