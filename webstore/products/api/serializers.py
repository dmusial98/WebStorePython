from ..models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productId', 'productName', 'productPrice', 'productStock', 'productDescription', 'productIcon', 'productStatus', 'categoryType', 'createTime', 'updateTime') # if not declared, all fields of the model will be shown