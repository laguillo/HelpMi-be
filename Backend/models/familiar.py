from django.db import models
from .user import User


class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.CharField('Nombre del paciente')
