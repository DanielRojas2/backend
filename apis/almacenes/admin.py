from django.contrib import admin
from .models.Almacen import Almacen
from .models.Estante import Estante
from .models.Nivel import Nivel
from .models.NivelEstante import NivelEstante

admin.site.register(Almacen)
admin.site.register(Estante)
admin.site.register(Nivel)
admin.site.register(NivelEstante)
