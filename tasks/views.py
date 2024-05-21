from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Usuarios
from .serializer import userSerializer

# Create your views here.
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):  # Agrega este método para aceptar solicitudes GET
        usuarios = Usuarios.objects.all()
        serializer = userSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')
        
        try:
            usuario = Usuarios.objects.get(correo=correo)
        except Usuarios.DoesNotExist:
            return Response({"error": "Correo o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not usuario.check_password(password):  # Assuming you have a method to check the password
            return Response({"error": "Correo o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = userSerializer(usuario)
        return Response(serializer.data)    