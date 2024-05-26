from django.contrib import admin
from .models import Facultad, Carrera, Tutor, Estudiante, Usuario, Avance
# Register your models here.
admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Tutor)
admin.site.register(Estudiante)
admin.site.register(Usuario)
admin.site.register(Avance)