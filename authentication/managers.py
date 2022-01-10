from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, cpf, password, **extra_fields):
        required_fields = [first_name, last_name, email, cpf]
        if not all(required_fields):
            raise ValueError("Email, Senha, CPF, Primeiro e Último nome são obrigatórios")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, cpf, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        superuser_fields = ['is_staff', 'is_superuser', 'is_active']

        if not all([extra_fields.get(key) for key in superuser_fields]):
            raise ValueError('is_staff, is_superuser and is_active must be True for superusers')

        return self.create_user(
            first_name=first_name, last_name=last_name, email=email, cpf=cpf, password=password, **extra_fields
        )
