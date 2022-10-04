from tkinter.font import families
from django.db import models
from Backend.models.historiaClinica import Signos_vitales

from Backend.models.paciente import Paciente
from .user import User, models

class Familiar(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)
    
    oximetria = models.DecimalField('Oximetria',max_digits=None,decimal_places=None)
    f_respiratoria = models.DecimalField('Frecuencia respiratoria', max_digits=None,decimal_places=None)
    f_cardiaca = models.DecimalField('Frecuencia cardiaca',max_digits=None,decimal_places=None)
    temperatura = models.DecimalField('Temperatura', max_digits=None,decimal_places=None)
    p_arterial = models.DecimalField('Presion arterial', max_digits=None,decimal_places=None)
    glicemias = models.DecimalField('Glicemias',max_digits=None,decimal_places=None)
    