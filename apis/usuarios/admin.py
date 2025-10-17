# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.PerfilUsuario import PerfilUsuario
from .admin_forms import PerfilUsuarioCreationForm, PerfilUsuarioChangeForm

class PerfilUsuarioAdmin(BaseUserAdmin):
    form = PerfilUsuarioChangeForm
    add_form = PerfilUsuarioCreationForm

    list_display = ('username', 'email', 'nombre', 'apellido_paterno', 'usuario_activo', 'usuario_admin')
    list_filter = ('usuario_activo', 'usuario_admin')
    readonly_fields = ('alta',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'cargo')}),
        ('Permisos', {'fields': ('usuario_activo', 'usuario_admin')}),
        ('Fechas', {'fields': ('alta', 'baja')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombre', 'apellido_paterno', 'apellido_materno', 'cargo', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email', 'nombre', 'apellido_paterno')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
