# admin_forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models.PerfilUsuario import PerfilUsuario

class PerfilUsuarioCreationForm(forms.ModelForm):
    """Formulario para crear nuevos usuarios en el admin con password hasheada"""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = PerfilUsuario
        fields = ['username', 'email', 'nombre', 'apellido_paterno', 'apellido_materno', 'cargo']

    def clean_password2(self):
        # Verifica que las contraseñas coincidan
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return p2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])  # hash correcto
        if commit:
            usuario.save()
        return usuario

class PerfilUsuarioChangeForm(forms.ModelForm):
    """Formulario para actualizar usuarios"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = PerfilUsuario
        fields = ['username', 'email', 'password', 'nombre', 'apellido_paterno', 'apellido_materno', 'usuario_activo', 'usuario_admin', 'cargo']
