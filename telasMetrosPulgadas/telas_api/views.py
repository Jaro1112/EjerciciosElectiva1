import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class calcularPulgadas(APIView):
    def get(self,request,*args,**kwargs):

        metros=request.GET.get('metros')
        cantidad=(float(metros))/(float(0.0254))
        return Response(cantidad,status=status.HTTP_200_OK)
    