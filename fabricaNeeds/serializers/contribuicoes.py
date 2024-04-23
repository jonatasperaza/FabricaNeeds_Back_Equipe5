from rest_framework.serializers import ModelSerializer

from fabricaNeeds.models import Contribuicoes, Contribuinte

class ContribuicoesSerializer(ModelSerializer):
    class Meta:
        model = Contribuicoes
        fields = "__all__"

class ContribuinteSerializer(ModelSerializer):
    class Meta:
        model = Contribuinte
        fields = "__all__"