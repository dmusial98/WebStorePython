from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=250)
    productPrice = models.IntegerField()
    productStock = models.IntegerField()
    productDescription = models.CharField(max_length=5000)
    productIcon = models.CharField(max_length=1000)
    productStatus = models.IntegerField()
    categoryType = models.IntegerField()
    createTime = models.CharField(max_length=30)
    updateTime = models.CharField(max_length=30)
    
    def __str__(self):
        return self.productName