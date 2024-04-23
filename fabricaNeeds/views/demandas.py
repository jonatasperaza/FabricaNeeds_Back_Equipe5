from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import Demandas
from fabricaNeeds.serializers import DemandasSerializer

class DemandasViewSet(ModelViewSet):
    queryset = Demandas.objects.all()
    serializer_class = DemandasSerializer