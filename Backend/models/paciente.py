from django.db import models

from .familiar import Familiar
from .user import User


#OneToOneField

class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario_p=models.ForeignKey(User, on_delete=models.CASCADE)
    
    familiar=models.ForeignKey(Familiar, on_delete=models.CASCADE)
