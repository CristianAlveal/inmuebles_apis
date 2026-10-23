from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from gestion_apis.permissions import EsArrendatario

from  gestion_apis.models.solicitud_arriendo import SolicitudArriendo
from gestion_apis.serializers import SolicitudArriendoSerializer


class SolicitudArriendoView(ListCreateAPIView):

    serializer_class = SolicitudArriendoSerializer
   # permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [EsArrendatario()]

        return [IsAuthenticated()]

    def get_queryset(self):
        # Cada arrendatario ve solamente sus solicitudes
        return SolicitudArriendo.objects.filter(
            arrendatario=self.request.user
        ).select_related('inmueble')

    def perform_create(self, serializer):
        # Asocia la solicitud al usuario autenticado
        serializer.save(
            arrendatario=self.request.user,
            estado='PENDIENTE'
        )