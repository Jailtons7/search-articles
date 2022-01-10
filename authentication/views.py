from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from authentication.serializers import ObtainTokenPairWithEmailSerializer
from authentication.serializers import CustomUserSerializer


class ObtainTokenPairsWithEmailView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ObtainTokenPairWithEmailSerializer


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
