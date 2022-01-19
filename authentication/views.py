from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from authentication.serializers import ObtainTokenPairWithEmailSerializer
from authentication.serializers import CustomUserSerializer


class ObtainTokenPairsWithEmailView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ObtainTokenPairWithEmailSerializer


class UserView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'cpf': user.cpf,
            'phone': user.phone,
            'full_name': user.get_full_name()
        }
        return Response(user_data, status=status.HTTP_200_OK)


class CreateCustomUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCustomUserView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccountView(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return Response({'message': 'Deleted account'}, status=status.HTTP_204_NO_CONTENT)
