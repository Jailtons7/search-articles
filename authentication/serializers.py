from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class ObtainTokenPairWithEmailSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(ObtainTokenPairWithEmailSerializer, cls).get_token(user)
        token['email'] = user.email
        return token
