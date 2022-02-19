# `from .models import CartProduct
# from ..carts.models import Cart
# from rest_framework import serializers

# class CartProductSerializer(serializers.HyperlinkedModelSerializer):

#     parent_id = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(),source='cart.id')

#     class Meta:
#         model = CartProduct
#         fields = ('id','productId', 'count', 'cart_id')

#     def create(self, validated_data):
#         subject = CartProduct.objects.create(parent=validated_data['cartId']['id'], productId=validated_data['productId'], count=validated_data['count'])

#         return cartProduct