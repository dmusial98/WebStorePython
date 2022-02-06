from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=5000)
    price = models.IntegerField()
    amount = models.IntegerField()
    
    def __str__(self):
        return self.name