from rest_framework import serializers
from .models import Facultad, Carrera, Tutor, Estudiante, Usuario, Avance

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '_all_'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '_all_'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '_all_'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '_all_'

class UsuarioSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer(source='id_tutor', read_only=True)
    class Meta:
        model = Usuario
        fields = '_all_'

class AvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avance
        fields = '_all_'

