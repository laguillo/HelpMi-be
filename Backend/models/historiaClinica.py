from django.db import models
from .user import User
from .paciente import Paciente
from .familiar import Familiar


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_h = models.ForeignKey(
        User, on_delete=models.CASCADE)
    paciente_h = models.ForeignKey(
        Paciente, on_delete=models.CASCADE)
    familiar = models.ForeignKey(
        Familiar, on_delete=models.CASCADE)
