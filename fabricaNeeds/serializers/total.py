from rest_framework.serializers import ModelSerializer

from fabricaNeeds.models import Total

class TotalSerializer(ModelSerializer):
    class Meta:
        model = Total
        fields = "__all__"