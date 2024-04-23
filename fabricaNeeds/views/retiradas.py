from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import Retiradas
from fabricaNeeds.serializers import RetiradasSerializer

class RetiradasViewSet(ModelViewSet):
    queryset = Retiradas.objects.all()
    serializer_class = RetiradasSerializer