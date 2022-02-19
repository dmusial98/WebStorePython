from django.db import models

class Cart(models.Model):
    userId = models.IntegerField()


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL, related_name='products')
    productId = models.IntegerField()
    count = models.PositiveIntegerField()
