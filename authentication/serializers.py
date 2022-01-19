import re

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


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'cpf', 'phone', 'first_name', 'last_name', 'password',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for field in self.Meta.fields:
            if field != 'password':
                setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()
        return instance

    def validate_cpf(self, value):
        """
        Check that cpf has only numbers
        """
        pattern = r'\d{11}'
        if not bool(re.match(pattern, value)):
            raise serializers.ValidationError('CPF must have only numbers')
        return value
