from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.usuarioViews import MiUsuarioView, UsuarioViewSet
from gestion_apis.views.inmuebleViews import  InmuebleViewSet
from gestion_apis.views.comuna_region_views import RegionListView, ComunaListView
from gestion_apis.views.solicitud_arriendo_views import   SolicitudArriendoView

router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet,
    basename='usuario'
)

router.register(
    r'inmuebles',
    InmuebleViewSet,
    basename='inmueble'
)

urlpatterns = [
    path(
        'mi-usuario/',
        MiUsuarioView.as_view(),
        name='mi_usuario'
    ),
    
    path('regiones/', RegionListView.as_view(), name='lista_regiones'),
    path('comunas/', ComunaListView.as_view(), name='lista_comunas'),
  
    path(
        'solicitudes-arriendo/',
        SolicitudArriendoView.as_view(),
        name='solicitudes_arriendo'
    ),

    path('', include(router.urls)),
]