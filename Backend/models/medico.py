from django.db import models
from .user import User, models

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        User, related_name='medico', on_delete=models.CASCADE)
    especialidad = models.CharField('Especialidad', max_length=45)
