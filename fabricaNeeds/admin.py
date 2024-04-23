from django.contrib import admin
from .models import Contribuicoes, Contribuinte, Total, Retiradas, Estoque, RetirarEstoque, Demandas,  EntradasEstoque

admin.site.register(Contribuicoes)
admin.site.register(Contribuinte)
admin.site.register(Total)
admin.site.register(Retiradas)
admin.site.register(Estoque)
admin.site.register(RetirarEstoque)
admin.site.register(Demandas)
admin.site.register(EntradasEstoque)