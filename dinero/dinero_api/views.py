import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class calcularDolares(APIView):
    def get(self,request,*args,**kwargs):

        COP=request.GET.get('COP')
        cantidad=(float(COP))/(float(3770.12))
        return Response(cantidad,status=status.HTTP_200_OK)
    