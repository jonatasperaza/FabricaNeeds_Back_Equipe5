from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import Estoque
from fabricaNeeds.serializers import EstoqueSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer