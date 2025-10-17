from rest_framework import permissions

class RolPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(view, "allowed_roles"):
            usuario = request.user
            if not usuario.is_authenticated:
                return False
            rol_usuario = getattr(usuario.cargo.rol, "rol", "").lower() if usuario.cargo else ""
            return rol_usuario in [r.lower() for r in view.allowed_roles]
        return True
