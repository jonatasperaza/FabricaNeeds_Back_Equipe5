from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import Contribuicoes, Contribuinte
from fabricaNeeds.serializers import ContribuicoesSerializer, ContribuinteSerializer

class ContribuicoesViewSet(ModelViewSet):
    queryset = Contribuicoes.objects.all()
    serializer_class = ContribuicoesSerializer

class ContribuinteViewSet(ModelViewSet):
    queryset = Contribuinte.objects.all()
    serializer_class = ContribuinteSerializer