import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class calcularPrecio(APIView):
    def get(self,request,*args,**kwargs):

        precioMin=request.GET.get('precioMin')
        minutos=request.GET.get('minutos')

        Preciofinal=(float(minutos)) * (float(precioMin))
        return Response(Preciofinal,status=status.HTTP_200_OK)
    