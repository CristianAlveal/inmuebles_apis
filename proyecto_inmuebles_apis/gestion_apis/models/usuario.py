from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='usuario'
    )
    
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20,blank=True)
    direccion = models.CharField(max_length=200, blank=True)
      # Opciones disponibles para el tipo de inmueble
    TIPOS_USUARIO = [
           ('Arrendatario', 'Arrendatario'),
           ('Arrendador', 'Arrendador'),
           
       ]
   
       # Tipo de usuario
    tipo_usuario = models.CharField(
           max_length=50,
           choices=TIPOS_USUARIO
       )   

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username