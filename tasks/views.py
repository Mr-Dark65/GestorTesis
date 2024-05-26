from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from .models import Usuario, Facultad, Carrera, Tutor, Estudiante, Avance
from .serializer import UsuarioSerializer, FacultadSerializer, CarreraSerializer, TutorSerializer, EstudianteSerializer, AvanceSerializer

# Create your views here.
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):  # Método para aceptar solicitudes GET
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')
        
        try:
            usuario = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            return Response({"error": "Correo o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not usuario.check_password(password):  # Asumiendo que tienes un método para verificar la contraseña
            return Response({"error": "Correo o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class AvanceViewSet(viewsets.ModelViewSet):
    queryset = Avance.objects.all()
    serializer_class = AvanceSerializer