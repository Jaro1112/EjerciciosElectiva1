from django.urls import path
from .views import calcularEdad

urlpatterns = [
    path('calcular',calcularEdad.as_view()),
]