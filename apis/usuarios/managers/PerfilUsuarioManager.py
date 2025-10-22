from django.contrib.auth.models import BaseUserManager

class PerfilUsuarioManager(BaseUserManager):
    def create_user(self, username, email, nombre, apellido_paterno, apellido_materno=None, baja=None, cargo=None, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico válido.")
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario válido.")
        
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            baja=baja,
            cargo=cargo
        )
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombre, apellido_paterno, apellido_materno=None, baja=None, cargo=None, password=None):
        usuario = self.create_user(
            email=email,
            username=username,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            baja=baja,
            cargo=cargo,
            password=password
        )
        usuario.usuario_admin = True
        usuario.save()
        return usuario
