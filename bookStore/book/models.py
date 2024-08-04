from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    biography = models.TextField()
    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.name} - {self.code}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=3)
    stock = models.IntegerField()
    country = models.ManyToManyField(Country)
    
    def __str__(self):
        return f'{self.title} - {self.author.name}'
    


    
