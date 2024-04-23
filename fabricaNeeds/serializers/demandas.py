from rest_framework.serializers import ModelSerializer

from fabricaNeeds.models import Demandas

class DemandasSerializer(ModelSerializer):
    class Meta:
        model = Demandas
        fields = "__all__"