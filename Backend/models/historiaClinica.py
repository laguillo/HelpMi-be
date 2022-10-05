from django.db import models


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.FloatField('Oximetria')
    f_respiratoria = models.FloatField('Frecuencia respiratoria')
    f_cardiaca = models.FloatField('Frecuencia cardiaca')
    temperatura = models.FloatField('Temperatura')
    p_arterial = models.FloatField('Presion arterial')
    glicemias = models.FloatField('Glicemias')
