from rest_framework import serializers
from .models import Facultad, Carrera, Tutor, Estudiante, Usuario, Avance

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer(source='id_tutor', read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

class AvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avance
        fields = '__all__'

