from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models.usuario import Usuario
from .models.inmueble import Inmueble
from .models.tipo_inmueble import Tipo_Inmueble
from .models.region import Region
from .models.comuna import Comuna
from .models.solicitud_arriendo import SolicitudArriendo
from django.db import transaction


class TipoInmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Inmueble
        fields = ['id', 'nombre']
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre']


class ComunaSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Comuna
        fields = ['id', 'nombre', 'region']


class PerfilUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [ 
            'id',
            'nombres',
            'apellidos',         
            'telefono',
            'direccion',
            'tipo_usuario',
        ]
        
class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True
    )

  

    usuario = PerfilUsuarioSerializer(required=True)

    class Meta:
        model = User
        fields = [ 
            'id',           
            'username',
            'password',
            'email',
            'first_name',
            'last_name',          
            'usuario'
        ]

    @transaction.atomic
    def create(self, validated_data):

        # Extraer los datos anidados del perfil
        perfil_data = validated_data.pop('usuario')

        password = validated_data.pop('password')
        
       
        # Obtener el tipo de usuario
        tipo_usuario = perfil_data.get('tipo_usuario')

        # Validar el tipo antes de crear los registros
        grupos_permitidos = {
            'Arrendador': 'Arrendador',
            'Arrendatario': 'Arrendatario',
        }

        if tipo_usuario not in grupos_permitidos:
            raise serializers.ValidationError({
                'usuario': {
                    'tipo_usuario':
                    'Debe ser Arrendador o Arrendatario.'
                }
            })


        user = User(**validated_data)

        user.set_password(password)
        user.save()

        Usuario.objects.create(
            usuario=user,
           **perfil_data
        )
        
          # Buscar el grupo correspondiente
        nombre_grupo = grupos_permitidos[tipo_usuario]
        grupo = Group.objects.get(name=nombre_grupo)

        # Asignar el usuario al grupo
        user.groups.add(grupo)


        return user
    
    
            
class InmuebleSerializer(serializers.ModelSerializer):
    
    
    comuna = ComunaSerializer(read_only=True)
    tipo_inmueble = TipoInmuebleSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Inmueble
        fields = [
            'id',
            'nombre',
            'descripcion',
            'm2_construidos',
            'm2_totales',
            'estacionamientos',
            'habitaciones',
            'banos',
            'direccion',
            'precio_mensual',
            'comuna',
            'tipo_inmueble',
            'usuario',
        ]
        read_only_fields = ['usuario']
        


class SolicitudArriendoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudArriendo
        fields = [
            'id',
            'inmueble',
            'arrendatario',
            'estado',
            'fecha_solicitud',
            'fecha_respuesta',
        ]

        read_only_fields = [
            'id',
            'arrendatario',
            'estado',
            'fecha_solicitud',
            'fecha_respuesta',
        ]