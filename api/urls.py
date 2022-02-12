from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'articles', views.ArtigosPublicadosViews)
router.register(r'articles/<int:pk>', views.ArtigosPublicadosViews)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard', views.DashboardView.as_view(), name='dashboard')
]
