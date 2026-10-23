from django.db import models
from .region import Region



class Comuna(models.Model):
    nombre =  nombre = models.CharField(max_length=50)
    
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='comunas'
    )
       
    def __str__(self):
        return self.nombre  