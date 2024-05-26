from django.db import models

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_facultad_pertenece = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='carreras')

    def __str__(self):
        return self.nombre

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    estado = models.CharField(max_length=50)
    tema_tesis = models.CharField(max_length=50, null=True, blank=True)
    id_tutor_pertenece = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='estudiantes')
    id_carrera_pertenece = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    id_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)

    def __str__(self):
        return self.nombre_usuario

class Avance(models.Model):
    id_avance = models.AutoField(primary_key=True)
    fecha_entrega = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    porcentaje_avance = models.IntegerField()
    documento_avance_url = models.CharField(max_length=50, null=True, blank=True)
    id_estudiante_pertenece = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='avances')

    def __str__(self):
        return f"Avance {self.id_avance} - {self.porcentaje_avance}%"
