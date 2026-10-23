from django.db import models
from gestion_apis.models.inmueble import Inmueble
from django.contrib.auth.models import User

class SolicitudArriendo(models.Model):
    
    ESTADOS= [ ('PENDIENTE', 'Pendiente'),
              ('ACEPTADA', 'Aceptada'),
              ('RECHAZADA', 'Rechazada'),
              ]
    
    inmueble = models.ForeignKey(Inmueble, on_delete= models.CASCADE, related_name='solicitudes')
    
    arrendatario = models.ForeignKey(User, on_delete= models.CASCADE, related_name='solicitudes_arriendo' )
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.inmueble.nombre} - {self.arrendatario} - {self.estado}"
    
    