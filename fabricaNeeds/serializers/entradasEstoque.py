from rest_framework.serializers import ModelSerializer

from fabricaNeeds.models import EntradasEstoque

class EntradasEstoqueSerializer(ModelSerializer):
    class Meta:
        model = EntradasEstoque
        fields = "__all__"