from django.contrib import admin
from .models.usuario import Usuario
from .models.tipo_inmueble import Tipo_Inmueble
from .models.inmueble import Inmueble
from .models.comuna import Comuna

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    # Mostrar el usuario asociado, pero impedir que se cambie
    readonly_fields = ('usuario',)

    list_display = (
        'usuario',
        'nombres',
        'apellidos',
        'tipo_usuario',
    )

    search_fields = (
        'usuario__username',
        'nombres',
        'apellidos',
    )


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):

    # Mostrar el usuario asociado, pero impedir que se cambie
    readonly_fields = ('usuario',)

    list_display = (       
        'nombre',
        'descripcion',
        'habitaciones',
        'direccion',
        'disponible',
        'comuna',
        'mostrar_region',
        'usuario',
    )

    search_fields = (
        'nombre',
        'habitaciones',
        'direccion',
    )
    
    @admin.display(description='Región')
    def mostrar_region(self, obj):
        return obj.comuna.region
    
admin.site.register(Tipo_Inmueble)

admin.site.register(Comuna)