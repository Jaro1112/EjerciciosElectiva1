from django.urls import path
from .views import calcularPrecio

urlpatterns = [
    path('calcular',calcularPrecio.as_view()),
]