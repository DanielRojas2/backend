from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis.usuarios'

    def ready(self):
        import apis.usuarios.signals
