import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class calcularEdad(APIView):
    def get(self,request,*args,**kwargs):
        
        dia =request.GET.get('dia')
        mes =request.GET.get('mes')
        anyo =request.GET.get('anyo')
        
        

        dias = (12 - int(dia)) 
        mezaco = (4 - int(mes))
        anyos = (2024 - int(anyo))

        
        if mezaco <0 and dias<0 :
            
            diasss = int(dia)-12
            dias = 30 - diasss

            meses = mezaco 
            mezaco = meses - 1

            anyaco = anyos
            anyos = anyaco - 1 
            
            mesesss = int(mes)-4
            mezaco = 12 - mesesss
            
        elif dias<0 :
            diasss = int(dia)-12
            dias = 30 - diasss

            meses = mezaco 
            mezaco = meses - 1
        elif mezaco<0 :
            anyaco = anyos
            anyos = anyaco - 1 
            
            mesesss = int(mes)-4
            mezaco = 12 - mesesss
        
        
            
        edad = f"el postulante tiene {dias} dias, {mezaco} meses y {anyos} anyos"
        return Response(edad,status=status.HTTP_200_OK)
    