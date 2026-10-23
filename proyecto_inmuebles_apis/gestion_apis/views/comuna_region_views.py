from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from gestion_apis.models.region import Region
from gestion_apis.models.comuna import Comuna
from gestion_apis.serializers import RegionSerializer, ComunaSerializer


class RegionListView(ListAPIView):
    queryset = Region.objects.all().order_by('nombre')
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]


class ComunaListView(ListAPIView):
    queryset = Comuna.objects.select_related('region').all().order_by('nombre')
    serializer_class = ComunaSerializer
    permission_classes = [AllowAny]