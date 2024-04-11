import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import math

class calcularPrecio(APIView):
    def get(self,request,*args,**kwargs):

        precioHora=request.GET.get('precioHora')
        horas=request.GET.get('horas')


        horastotales= math.ceil(float(horas))
        Preciofinal=(int(horastotales)) * (int(precioHora))
        return Response(Preciofinal,status=status.HTTP_200_OK)
    