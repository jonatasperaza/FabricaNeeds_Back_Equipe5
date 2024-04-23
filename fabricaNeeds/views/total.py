from rest_framework.viewsets import ModelViewSet

from fabricaNeeds.models import Total
from fabricaNeeds.serializers import TotalSerializer

class TotalViewSet(ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer