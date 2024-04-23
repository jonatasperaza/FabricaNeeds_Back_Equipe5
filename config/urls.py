from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from fabricaNeeds.views import TotalViewSet, EstoqueViewSet, DemandasViewSet, RetiradasViewSet, RetirarEstoqueViewSet, EntradasEstoqueViewSet, ContribuinteViewSet, ContribuicoesViewSet

router = DefaultRouter()
router.register(r"total", TotalViewSet)
router.register(r"estoque", EstoqueViewSet)
router.register(r"demandas", DemandasViewSet)
router.register(r"retiradas", RetiradasViewSet)
router.register(r"retirarEstoque", RetirarEstoqueViewSet)
router.register(r"entradasEstoque", EntradasEstoqueViewSet)
router.register(r"contribuinte", ContribuinteViewSet)
router.register(r"contribuicoes", ContribuicoesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
