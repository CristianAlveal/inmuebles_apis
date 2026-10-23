from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion_apis.serializers import InmuebleSerializer
from gestion_apis.models.inmueble import Inmueble
from gestion_apis.permissions import EsArrendador



class InmuebleViewSet(viewsets.ModelViewSet):
    """
    API REST para administrar inmuebles.

    Operaciones disponibles:
    - Listar inmuebles
    - Consultar un inmueble
    - Crear un inmueble
    - Actualizar un inmueble
    - Eliminar un inmueble
    """

    queryset = Inmueble.objects.all()

    serializer_class = InmuebleSerializer

    # Para este ejemplo educativo:
    permission_classes = [EsArrendador]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
        
    

