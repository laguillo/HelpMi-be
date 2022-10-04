from django.contrib import admin

from Backend.models import historiaClinica
from Backend.models.familiar import Familiar
from .models.user import User
from .models.medico import Medico
from .models.paciente import Paciente

# Register your models here.
admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(historiaClinica)
admin.site.register(Familiar)
