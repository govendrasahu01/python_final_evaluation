from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

class home(viewsets.ViewSet):
    def list(self,request):
        return Response({"massage":"DRF setup done"})