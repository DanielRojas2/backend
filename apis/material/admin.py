from django.contrib import admin
from .models.PartidaPresupuestaria import PartidaPresupuestaria
from .models.Presentacion import Presentacion
from .models.UdM import UdM
from .models.Material import Material

admin.site.register(PartidaPresupuestaria)
admin.site.register(Presentacion)
admin.site.register(UdM)
admin.site.register(Material)
