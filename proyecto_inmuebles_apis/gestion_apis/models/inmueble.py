from django.db import models
from django.contrib.auth.models import User
from gestion_apis.models.comuna import Comuna
from gestion_apis.models.tipo_inmueble import Tipo_Inmueble


# Create your models here.
class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()  
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)

    comuna = models.ForeignKey( Comuna,on_delete=models.PROTECT,
        related_name='inmuebles'
    )
    
    # Tipo de inmueble
    tipo_inmueble = models.ForeignKey(
        Tipo_Inmueble,
        on_delete=models.PROTECT,
        related_name='inmuebles'
       
    ) 
    
    precio_mensual = models.DecimalField(
        max_digits=10,
        decimal_places=2,      
    )
    
    disponible = models.BooleanField(default=True)
     
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='inmuebles'
    )
        
      
    def __str__(self):
        return self.nombre  