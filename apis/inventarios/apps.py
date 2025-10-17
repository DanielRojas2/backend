from django.apps import AppConfig


class InventariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis.inventarios'

    def ready(self):
        import apis.inventarios.signals
