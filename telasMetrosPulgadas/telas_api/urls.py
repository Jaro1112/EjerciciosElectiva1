from django.urls import path
from .views import calcularPulgadas

urlpatterns = [
    path('calcular',calcularPulgadas.as_view()),
]