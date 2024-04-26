from rest_framework.serializers import ModelSerializer
from fabricaNeeds.models import Contribuinte

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Contribuinte
        fields = ['nome', 'senha']
