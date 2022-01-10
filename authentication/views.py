from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from authentication.serializers import ObtainTokenPairWithEmailSerializer


class ObtainTokenPairsWithEmailView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ObtainTokenPairWithEmailSerializer
