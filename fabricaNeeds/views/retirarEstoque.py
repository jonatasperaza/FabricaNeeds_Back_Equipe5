from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import RetirarEstoque
from fabricaNeeds.serializers import RetirarEstoqueSerializer

class RetirarEstoqueViewSet(ModelViewSet):
    queryset = RetirarEstoque.objects.all()
    serializer_class = RetirarEstoqueSerializer