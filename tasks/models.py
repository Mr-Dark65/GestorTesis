from django.db import models

# Create your models here.
class Usuarios(models.Model):
    Nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nombre