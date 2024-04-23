from rest_framework.serializers import ModelSerializer

from fabricaNeeds.models import Retiradas

class RetiradasSerializer(ModelSerializer):
    class Meta:
        model = Retiradas
        fields = "__all__"