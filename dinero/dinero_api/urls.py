from django.urls import path
from .views import calcularDolares

urlpatterns = [
    path('calcular',calcularDolares.as_view()),
]