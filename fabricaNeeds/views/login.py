from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from fabricaNeeds.models import Contribuinte
from fabricaNeeds.serializers import LoginSerializer
from django.contrib.auth.hashers import make_password, check_password

class loginViewSet(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            senha = serializer.validated_data['senha']
            hashed_password = make_password(senha)

            # Buscar o contribuinte pelo nome de usuário
            try:
                contribuinte = Contribuinte.objects.get(nome=nome)
            except Contribuinte.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(senha, hashed_password):

                return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)