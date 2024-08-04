from rest_framework import serializers
from .models import *

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'birthdate',
            'biography',
        ]
        
class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    