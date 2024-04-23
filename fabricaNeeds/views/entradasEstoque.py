from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import EntradasEstoque
from fabricaNeeds.serializers import EntradasEstoqueSerializer

class EntradasEstoqueViewSet(ModelViewSet):
    queryset = EntradasEstoque.objects.all()
    serializer_class = EntradasEstoqueSerializer