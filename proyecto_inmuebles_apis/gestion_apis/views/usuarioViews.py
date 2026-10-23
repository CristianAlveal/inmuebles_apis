from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from gestion_apis.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UsuarioSerializer

    # Para este ejemplo educativo:
    permission_classes = [AllowAny]


class MiUsuarioView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):       
        serializer = UsuarioSerializer(
            request.user
        )

        return Response(serializer.data)
