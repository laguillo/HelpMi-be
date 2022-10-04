from django.db import models



from .user import User

class Familiar(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    oximetria = models.FloatField('Oximetria')
    f_respiratoria = models.FloatField('Frecuencia respiratoria')
    f_cardiaca = models.FloatField('Frecuencia cardiaca')
    temperatura = models.FloatField('Temperatura')
    p_arterial = models.FloatField('Presion arterial')
    glicemias = models.FloatField('Glicemias')
    