from .models import Cart, CartProduct
from rest_framework import serializers


class CartProductSerializer(serializers.HyperlinkedModelSerializer):

    cartId = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(),source='cart.id')

    class Meta:
        model = CartProduct
        fields = ('id','productId', 'count', 'cartId')

    def create(self, validated_data):
        subject = CartProduct.objects.create(cart=validated_data['cart']['id'], productId=validated_data['productId'], count=validated_data['count'])

        return subject
        

class CartSerializer(serializers.HyperlinkedModelSerializer):
    products = CartProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ('userId','id','products')


