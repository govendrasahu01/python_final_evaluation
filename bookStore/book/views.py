from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import *
from django.shortcuts import get_object_or_404
# Create your views here.
# book_by_country
class book_by_country(viewsets.ViewSet):
    def list(self,request):        
        id = request.pk
        data = Book.objects.filter(country = id)
        
        serializer = book_serializer(data, many = True)
        return Response({"Books in this country":serializer.data})

class home(viewsets.ViewSet):
    def list(self,request):
        data = Book.objects.all()
        serializer = book_serializer(data, many = True)
        return Response({"all Books":serializer.data})
        
    
class register_user(viewsets.ViewSet):
    def create(self,request):
        data = request.data
        serializer = user_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'massage':'user successfully registered',"user":serializer.data})
        
        return Response({'massage':serializer.errors})
        