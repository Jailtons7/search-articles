from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import (
    ObtainTokenPairsWithEmailView,
    CreateCustomUserView,
    UpdateCustomUserView,
    UserView,
    DeleteAccountView,
)


urlpatterns = [
    path('users/', UserView.as_view(), name='get_user'),
    path('users/create/', CreateCustomUserView.as_view(), name='create_user'),
    path('users/update/', UpdateCustomUserView.as_view(), name='update_user'),
    path('users/delete/', DeleteAccountView.as_view(), name='update_user'),
    path('token/obtain/', ObtainTokenPairsWithEmailView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
