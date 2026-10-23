
from rest_framework.permissions import BasePermission, SAFE_METHODS


class EsArrendador(BasePermission):
    """
    Permite crear inmuebles solo a usuarios autenticados
    que pertenezcan al grupo Arrendador.
    """

    message = "Solo los usuarios con rol Arrendador pueden crear inmuebles."

    def has_permission(self, request, view):

        # Consultas GET, HEAD y OPTIONS permitidas
        if request.method in SAFE_METHODS:
            return True

        # Se requiere iniciar sesión
        if not request.user or not request.user.is_authenticated:
            return False

        # Solo Arrendador puede crear, editar o eliminar
        return request.user.groups.filter(
            name="Arrendador"
        ).exists()



class EsArrendatario(BasePermission):

    message = "Solo los arrendatarios pueden solicitar inmuebles."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(
                name="Arrendatario"
            ).exists()
        )