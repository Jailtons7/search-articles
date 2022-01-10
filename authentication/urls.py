from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import ObtainTokenPairsWithEmailView, CreateCustomUserView


urlpatterns = [
    path('user/create/', CreateCustomUserView.as_view(), name='create_user'),
    path('token/obtain/', ObtainTokenPairsWithEmailView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
