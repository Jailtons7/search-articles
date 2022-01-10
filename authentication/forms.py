from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'cpf', 'first_name', 'last_name',)


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'cpf', 'first_name', 'last_name',)
