from django.db import models

# Create your models here.

class Category(models.Model):
    name                =  models.CharField(max_length=65)

    def __str__(self):
        return str(self.name)
    

class Vehicles(models.Model):
    name                =   models.CharField(max_length=100)
    imagen              =   models.ImageField(upload_to='vehiculos/')
    price               =   models.DecimalField(max_digits=10, decimal_places=2)
    year_of_production  =   models.PositiveIntegerField()
    category            =   models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)



